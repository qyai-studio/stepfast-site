/* Small, dependency-free tools. Each tool is a <section data-tool="..."> in the page. */
(function () {
  "use strict";

  function $(root, sel) { return root.querySelector(sel); }
  function fmtTime(totalMinutes) {
    var m = ((Math.round(totalMinutes) % 1440) + 1440) % 1440;
    var h = Math.floor(m / 60), mm = m % 60;
    var suffix = h >= 12 ? "PM" : "AM";
    var h12 = h % 12 === 0 ? 12 : h % 12;
    return h12 + ":" + (mm < 10 ? "0" : "") + mm + " " + suffix;
  }
  function fmtHours(mins) {
    var h = Math.floor(mins / 60), m = Math.round(mins % 60);
    var out = [];
    if (h) out.push(h + " hr");
    if (m) out.push(m + " min");
    return out.join(" ") || "0 min";
  }
  function fmtNum(n) { return Math.round(n).toLocaleString("en-US"); }

  /* ---------- Fasting window planner ---------- */
  function fastingPlanner(root) {
    var out = $(root, ".result");
    var form = $(root, "form");
    function run(e) {
      if (e) e.preventDefault();
      var mode = form.elements.mode.value;
      var t = form.elements.time.value;
      var fastH = parseInt(form.elements.fast.value, 10);
      if (!t) { out.innerHTML = '<span class="err">Enter a time first.</span>'; return; }
      var parts = t.split(":");
      var at = parseInt(parts[0], 10) * 60 + parseInt(parts[1], 10);
      var eatMin = (24 - fastH) * 60;
      var start, end;
      if (mode === "first") { start = at; end = at + eatMin; }
      else { end = at; start = at - eatMin; }
      var html = "<p><strong>Eat between " + fmtTime(start) + " and " + fmtTime(end) + ".</strong></p>" +
        "<p>Fast from " + fmtTime(end) + " until " + fmtTime(start + 1440) + " the next day (" + fastH + " hours). " +
        "Your daily eating window is " + fmtHours(eatMin) + ".</p>";
      if (fastH > 16) {
        html += '<p class="err">Longer fasts are not necessarily better. Talk to a doctor before fasting this long.</p>';
      }
      out.innerHTML = html;
    }
    form.addEventListener("submit", run);
    form.addEventListener("input", run);
    run();
  }

  /* ---------- Step goal ramp planner ---------- */
  function stepGoal(root) {
    var out = $(root, ".result");
    var form = $(root, "form");
    function run(e) {
      if (e) e.preventDefault();
      var cur = parseInt(form.elements.current.value, 10);
      var goal = parseInt(form.elements.goal.value, 10);
      var inc = parseInt(form.elements.inc.value, 10);
      if (isNaN(cur) || isNaN(goal) || cur < 0 || goal < 1 || cur > 40000 || goal > 40000) {
        out.innerHTML = '<span class="err">Enter step counts between 0 and 40,000.</span>';
        return;
      }
      if (goal <= cur) {
        out.innerHTML = "<p><strong>You already average at least " + fmtNum(goal) + " steps a day.</strong> " +
          "You could keep this level, or choose a higher target.</p>";
        return;
      }
      var weeks = Math.ceil((goal - cur) / inc);
      var rows = "";
      var shown = Math.min(weeks, 26);
      for (var w = 1; w <= shown; w++) {
        var v = Math.min(cur + inc * w, goal);
        rows += "<tr><td>Week " + w + "</td><td>" + fmtNum(v) + " steps a day</td></tr>";
      }
      var more = weeks > 26 ? "<p class=\"meta\">Showing the first 26 weeks of " + weeks + ".</p>" : "";
      out.innerHTML = "<p><strong>About " + weeks + " week" + (weeks === 1 ? "" : "s") + " to reach " + fmtNum(goal) +
        " steps a day</strong> at +" + fmtNum(inc) + " steps a day each week.</p>" +
        '<div class="tablewrap"><table><thead><tr><th>When</th><th>Daily step target</th></tr></thead><tbody>' + rows +
        "</tbody></table></div>" + more +
        '<p class="meta">This is a pacing plan, not a prediction. It does not estimate weight change.</p>';
    }
    form.addEventListener("submit", run);
    form.addEventListener("input", run);
    run();
  }

  /* ---------- Step gap math (mirrors the rules in the app) ---------- */
  function stepGap(root) {
    var out = $(root, ".result");
    var form = $(root, "form");
    var perMin = parseFloat(root.getAttribute("data-walk-steps-per-min"));
    var delayPer1000 = parseFloat(root.getAttribute("data-delay-min-per-1000"));
    var capH = parseFloat(root.getAttribute("data-cap-hours"));
    function run(e) {
      if (e) e.preventDefault();
      var goal = parseInt(form.elements.goal.value, 10);
      var steps = parseInt(form.elements.steps.value, 10);
      if (isNaN(goal) || isNaN(steps) || goal < 1 || steps < 0) {
        out.innerHTML = '<span class="err">Enter your goal and today\'s steps.</span>';
        return;
      }
      var gap = goal - steps;
      if (gap <= 0) {
        out.innerHTML = "<p><strong>You're at or above your goal.</strong> Nothing to make up today.</p>";
        return;
      }
      var walkMin = gap / perMin;
      var delayMin = (gap / 1000) * delayPer1000;
      out.innerHTML = "<p><strong>You're " + fmtNum(gap) + " steps short.</strong></p>" +
        "<ul><li>Walk about <strong>" + fmtHours(walkMin) + "</strong> at " + fmtNum(perMin) + " steps a minute, or</li>" +
        "<li>if you can't walk, and fasting is on for you, push your first meal later by about <strong>" +
        fmtHours(delayMin) + "</strong>.</li></ul>" +
        '<p class="meta">The app never schedules more than ' + capH + " hours of total fasting in a day, whatever the gap.</p>";
    }
    form.addEventListener("submit", run);
    form.addEventListener("input", run);
    run();
  }

  var tools = { "fasting-planner": fastingPlanner, "step-goal": stepGoal, "step-gap": stepGap };
  document.querySelectorAll("[data-tool]").forEach(function (el) {
    var fn = tools[el.getAttribute("data-tool")];
    if (fn) fn(el);
  });
})();

