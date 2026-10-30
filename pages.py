"""Page content. Each page is a dict consumed by build.py.
Rules: no outcome promises, no before/after claims, health statements cite a source, StepFast facts come from config.py."""
import config as C
from config import app_link

SRC_CDC_ADULT = ("CDC: Adult Activity, an Overview (reviewed Dec 20, 2023)", "https://www.cdc.gov/physical-activity-basics/guidelines/adults.html")
SRC_CDC_COUNTS = ("CDC: What Counts as Physical Activity for Adults (reviewed Dec 6, 2023)", "https://www.cdc.gov/physical-activity-basics/adding-adults/what-counts.html")
SRC_HOPKINS = ("Johns Hopkins Medicine: Intermittent Fasting, What Is It, and How Does It Work? (updated Apr 7, 2026)", "https://www.hopkinsmedicine.org/health/expert-qa/intermittent-fasting-what-is-it-and-how-does-it-work")
SRC_MAYO = ("Mayo Clinic News Network: Is intermittent fasting good for weight loss? (Aug 26, 2022)", "https://newsnetwork.mayoclinic.org/discussion/mayo-clinic-q-and-a-is-intermittent-fasting-good-for-weight-loss/")


def cta(slug, label="Get StepFast on the App Store", extra=""):
    return f'<a class="btn" href="{app_link(slug)}" rel="noopener">{label}</a>{extra}'


def cta_band(slug, heading="Try it on your iPhone", text=None):
    text = text or f"StepFast is for adults {C.MIN_AGE}+ on iOS {C.MIN_IOS} or later. No account needed."
    return f'<aside class="cta-band"><h2>{heading}</h2><p>{text}</p>{cta(slug)}</aside>'


def faq(items):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)


SAFETY_NOTE = (
    '<p class="note warn"><strong>Not medical advice.</strong> Fasting is not right for everyone. '
    'If you are under 18, pregnant or breastfeeding, have a history of disordered eating, or have a medical '
    'condition (especially diabetes or anything involving medication), talk to a doctor before fasting. '
    '<a href="/safety/">Read the full safety page.</a></p>'
)

FASTING_FAQ = [
    ("Does StepFast require fasting?", "No. Step tracking, weight tracking and your daily plan work without it. Fasting is an optional feature, and StepFast's safety check can keep it switched off for you."),
    ("Can I add steps manually?", "Yes. You can connect Apple Health (read-only, optional) or enter steps yourself."),
    ("Does StepFast need an account?", "No. There is no StepFast account. Your plan and data are stored on your iPhone."),
    ("What iPhone do I need?", f"StepFast needs iOS {C.MIN_IOS} or later and is for adults {C.MIN_AGE} and older. The interface is in English."),
    ("Does StepFast give medical advice?", "No. It is a wellness app, not a medical device. It cannot diagnose, treat or replace advice from your doctor."),
    ("Where is my data stored?", f'On your phone. See the <a href="{C.LEGAL_PRIVACY}">privacy policy</a> for exactly what is and is not collected.'),
]


def home_body():
    return f"""
<section class="hero">
  <p class="meta">For iPhone · adults {C.MIN_AGE}+</p>
  <h1>A weight plan built around walking, with fasting optional</h1>
  <p class="lede">StepFast sets a daily step goal. If you fall short, it suggests a walk, or an optional later first meal.
  It tracks your steps and your weight, and needs no account.</p>
  <p>{cta('home')}<a class="btn ghost" href="/how-it-works/">See how it works</a></p>
  <ul class="facts">
    <li>iOS {C.MIN_IOS}+</li><li>No account</li><li>Data stays on your iPhone</li>
    <li>Apple Health is optional</li><li>Free, with an optional paid tier</li>
  </ul>
</section>

<h2>Your steps are the starting point</h2>
<p>StepFast reads your steps from Apple Health if you allow it, or you can enter them yourself. It compares today's
count with your daily goal and shows where you are. In the app the starting estimate is {C.DEFAULT_GOAL:,} steps, and
the zones look like this:</p>
<ul class="zones">
  <li><span class="dot r"></span> Under 3,000: below today's goal</li>
  <li><span class="dot o"></span> 3,000 to 5,000: almost at today's goal</li>
  <li><span class="dot y"></span> 5,000 to 7,000: at today's goal</li>
  <li><span class="dot g"></span> Over 7,000: above today's goal</li>
</ul>
<p class="meta">Example with the {C.DEFAULT_GOAL:,}-step starting estimate. Your own goal is personal.</p>

<h2>Track your weight over time</h2>
<p>Log your weight and watch the trend, not the single number. Day-to-day weight moves around, so a trend over
weeks tells you more than one morning's reading. StepFast also shows your steps and weight together so you can see how
your walking habit and the scale line up for you. <a href="/weight-tracking/">Learn how to track weight and read the trend.</a></p>

<h2>Fasting is optional</h2>
<p>Walking and weight tracking work without it. If you choose to use fasting, StepFast runs a safety check first and
keeps the feature off when that check says it should be. When you are short on steps the app leads with walking; if
you can't walk, an optional later first meal is the alternative. The app never plans more than {C.FAST_CAP_HOURS} hours
of total fasting in a day. <a href="/intermittent-fasting/">Learn about intermittent fasting</a> or
<a href="/safety/">read about safety</a>.</p>

<h2>Your data stays on your iPhone</h2>
<p>There is no StepFast account, and your plan and entries are stored on your phone. Apple Health access is optional and
read-only. Read the <a href="{C.LEGAL_PRIVACY}">privacy policy</a> for the details.</p>

<h2>Questions</h2>
{faq(FASTING_FAQ)}
{cta_band('home')}
"""


def how_body():
    return f"""
<p class="answer">StepFast compares your steps with a daily goal. If you're short, it shows what a walk would take. If
you can't walk and fasting is on for you, it can suggest a later first meal instead.</p>

<h2>1. Set up</h2>
<p>You confirm you are {C.MIN_AGE} or older and enter your height and weight, in pounds or kilograms. There's no account to
create. Apple Health is optional: allow it to read steps, weight and workouts, or enter steps yourself.</p>

<h2>2. Your daily goal and zones</h2>
<p>The app starts with an estimate of {C.DEFAULT_GOAL:,} steps a day and shows four zones around it: below, almost at, at,
and above your goal. As you log steps and weigh-ins, StepFast can estimate the range of daily steps where your own weight
holds steady. Some features, such as trends, are part of an optional paid tier; the App Store listing shows what is
included.</p>

<h2>3. If you're short on steps</h2>
<p>StepFast turns the gap into something concrete. Walking comes first. At {C.WALK_STEPS_PER_MIN} steps a minute,
every 1,000 steps is about {1000 // C.WALK_STEPS_PER_MIN} minutes of walking. On days you can't walk, and only if fasting
is on for you, the app can instead suggest a later first meal: about {C.LATER_BREAKFAST_MIN_PER_1000} minutes later for each
1,000 steps short, never pushing total fasting past {C.FAST_CAP_HOURS} hours in a day.</p>

<section class="tool" data-tool="step-gap" data-walk-steps-per-min="{C.WALK_STEPS_PER_MIN}" data-delay-min-per-1000="{C.LATER_BREAKFAST_MIN_PER_1000}" data-cap-hours="{C.FAST_CAP_HOURS}">
  <h3>Try the step-gap math</h3>
  <form>
    <div class="row">
      <label class="field"><span>Your daily goal (steps)</span><input type="number" name="goal" inputmode="numeric" min="1" max="40000" value="{C.DEFAULT_GOAL}"></label>
      <label class="field"><span>Steps so far today</span><input type="number" name="steps" inputmode="numeric" min="0" max="40000" value="3000"></label>
    </div>
  </form>
  <div class="result" aria-live="polite"></div>
</section>

<h2>4. Fasting is a choice, and a safety check comes first</h2>
<p>Fasting is optional and off until you choose it. StepFast asks a few safety questions first and can keep fasting
turned off for you. If you've told it about eating struggles, it doesn't push fasting. See
<a href="/safety/">who shouldn't fast</a>.</p>

<h2>5. Check in on trends</h2>
<p>The app has four tabs: Today, Calculator, Fast and Trends. Today shows your steps and plan, Fast is the optional timer,
and Trends shows your weight and steps over time. Read our <a href="/weight-tracking/">weight tracking guide</a> for tips on weigh-in routines and daily fluctuations.</p>
{SAFETY_NOTE}
{cta_band('how-it-works')}
"""


def weight_tracking_body():
    return f"""
<p class="answer"><strong>How should you track your weight?</strong> Use a routine you can follow without judging yourself by one reading. Daily and weekly weigh-ins are both used; consistency and how the process affects you matter. A weight trend is more useful than treating each number as a verdict.</p>

<h2>How often should I weigh myself?</h2>
<p>There is no single schedule that suits everyone. NIDDK lists weekly weight monitoring as one part of a structured, safe weight-management program. Cleveland Clinic notes that some people prefer a daily routine and others a weekly one. Choose a cadence that feels manageable. If weighing causes anxiety or pushes you toward restrictive behavior, scale back or pause and talk with a health professional.</p>

<h2>Make weigh-ins easier to compare</h2>
<ol>
  <li>Use the same scale on a firm, level surface.</li>
  <li>Weigh at a similar time and in similar clothing, if you choose to weigh regularly.</li>
  <li>Record the date with the measurement so you can compare readings across weeks.</li>
</ol>
<p>Consistency reduces avoidable differences between readings. Cleveland Clinic suggests weighing in the morning after using the restroom and before eating or drinking, but the most useful routine is one you can keep without distress.</p>

<h2>Why can weight change from one day to the next?</h2>
<p>The scale measures total body weight, which can shift for reasons besides a change in body fat. Water retention, food and digestion, physical activity, hormonal changes, stress and some medications can affect short-term readings. If your weight changes suddenly by a large amount without an obvious reason, ask a healthcare professional.</p>

<h2>Read the pattern, not one number</h2>
<p>If you weigh more often, look at the overall direction across several weeks rather than reacting to the highest or lowest day. If you weigh weekly, compare readings taken on similar days and conditions. A graph or trend line can make the pattern easier to see, but it cannot explain the cause of a change or predict a health outcome.</p>
<p>Progress also includes habits you can sustain. StepFast puts weight and step history together so you can review both. Its trend features are part of an optional paid tier; the App Store purchase screen shows current plan details.</p>

<h2>What StepFast tracks</h2>
<ul>
  <li>Weight and step information together, with optional read-only Apple Health access.</li>
  <li>Your plan and entries stored on your iPhone; no StepFast account is required.</li>
  <li>Step tracking and weight tracking without a food or calorie log. StepFast is a wellness app, not medical advice.</li>
</ul>
<p>See <a href="/how-it-works/">how StepFast works</a> or read the <a href="{C.LEGAL_PRIVACY}">privacy policy</a> for details about data handling.</p>

<h2>Common questions</h2>
{faq([
    ("Should I weigh myself daily or weekly?", "Either can work for different people. NIDDK describes weekly weight monitoring as a component of structured weight-management programs. Pick a consistent schedule that does not cause distress."),
    ("Why did my weight go up overnight?", "Short-term changes can reflect water retention, food and digestion, activity, hormones, stress or medication effects. A single reading cannot identify the cause."),
    ("Is daily weighing better for tracking progress?", "Daily readings give more points for a trend, but they are not right for everyone. If the scale affects your mood or behavior, use a less frequent schedule or pause tracking and seek support."),
    ("Can StepFast read weight from Apple Health?", "Yes. Apple Health access is optional and read-only. StepFast does not require an account, and your plan and entries are stored on your iPhone."),
    ("Does StepFast track calories or food?", "No. StepFast tracks steps and weight, with intermittent fasting as an optional feature. It is not a food or calorie log."),
])}

<h2>Sources</h2>
<ul class="sources">
  <li><a href="https://www.niddk.nih.gov/health-information/weight-management/adult-overweight-obesity/treatment">NIDDK: Treatment for Overweight &amp; Obesity</a></li>
  <li><a href="https://health.clevelandclinic.org/when-is-the-best-time-to-weigh-yourself">Cleveland Clinic: The Best Time to Weigh Yourself</a></li>
  <li><a href="https://health.clevelandclinic.org/weight-fluctuations">Cleveland Clinic: Why Weight Fluctuates</a></li>
</ul>
<p class="meta">This page is general wellness information, not a personal weight-management plan or medical advice.</p>
{cta_band('weight-tracking')}
"""


def safety_body():
    return f"""
<p class="answer">StepFast is for adults {C.MIN_AGE}+. It is a wellness app, not a medical device, and it doesn't give
medical advice. Fasting is optional, and a safety check can keep it off.</p>

<h2>Who should not fast, or should ask a doctor first</h2>
<ul>
  <li><strong>Under 18.</strong> StepFast is for adults only.</li>
  <li><strong>Pregnant or breastfeeding.</strong></li>
  <li><strong>A history of disordered eating.</strong> Strict fasting windows can trigger or worsen restrictive or obsessive eating.</li>
  <li><strong>Diabetes, especially if you take insulin or other glucose-lowering medication.</strong> Fasting can cause unsafe low blood sugar.</li>
  <li><strong>Any other medical condition or regular medication.</strong> Check with your doctor first.</li>
</ul>
<p>These points follow guidance from <a href="{SRC_HOPKINS[1]}">Johns Hopkins Medicine</a> and
<a href="{SRC_MAYO[1]}">Mayo Clinic</a>. Longer fasts of 24 hours or more are not necessarily better, and Johns Hopkins
says they may be dangerous.</p>

<h2>What StepFast does about it</h2>
<ul>
  <li>Fasting is off until you choose it.</li>
  <li>A safety check runs first and can keep fasting switched off.</li>
  <li>The app never plans more than {C.FAST_CAP_HOURS} hours of total fasting in a day.</li>
  <li>Walking is the first suggestion when you're short on steps.</li>
</ul>

<h2>Stop and get help if</h2>
<ul>
  <li>You feel faint, confused, or very unwell, or develop unusual symptoms. Stop fasting, eat, and contact a clinician. In an emergency, call your local emergency number (911 in the US).</li>
  <li>Food, weight, or fasting is starting to feel stressful or out of control. The <a href="https://www.allianceforeatingdisorders.com/">National Alliance for Eating Disorders</a> offers support and resources.</li>
</ul>
<p>Not sure whether fasting is right for you? Use StepFast for walking and weight tracking only. Fasting can stay off.</p>
<h2>Sources</h2>
<ul class="sources"><li><a href="{SRC_HOPKINS[1]}">{SRC_HOPKINS[0]}</a></li><li><a href="{SRC_MAYO[1]}">{SRC_MAYO[0]}</a></li></ul>
{cta_band('safety')}
"""


def fasting_pillar_body():
    return f"""
<p class="answer"><strong>Intermittent fasting</strong> means cycling between eating and not eating on a schedule. It is
optional in StepFast. It isn't right for everyone, and it isn't necessary for walking and weight tracking.</p>
{SAFETY_NOTE}

<h2>Common ways people do it</h2>
<ul>
  <li><strong>Daily time-restricted eating.</strong> Eating only within a window of about six to eight hours a day. 16/8 is the usual example: an eight-hour eating window and a 16-hour fast.</li>
  <li><strong>5:2.</strong> Eating normally five days a week and eating one small meal on the other two.</li>
</ul>
<p>Johns Hopkins Medicine describes these patterns, and notes that fasts of 24 hours or longer are "not necessarily better
for you, and may be dangerous."</p>
<p>Ready to plan a daily window? Use the <a href="/intermittent-fasting/schedule/">fasting schedule planner</a>.</p>

<h2>What research suggests</h2>
<p>Mayo Clinic says alternate-day fasting is about as effective as a typical low-calorie diet for weight loss, and that
eating fewer calories than you burn remains the basis of losing weight. Short-term benefits are possible, but little
long-term research exists, so long-term benefits and risks are unknown. Common side effects include hunger, fatigue and
headaches. See <a href="/intermittent-fasting/weight-loss/">fasting and weight loss</a> for more.</p>

<h2>How StepFast treats fasting</h2>
<p>It is a choice, not the plan. StepFast leads with walking. If you're short on steps and can't walk, and fasting is on
for you, it can suggest a later first meal. A safety check comes first, and total fasting never goes past
{C.FAST_CAP_HOURS} hours in a day. Read about <a href="/intermittent-fasting/walking-while-fasting/">walking while fasting</a>.</p>

<h2>Keep reading</h2>
<ul>
  <li><a href="/intermittent-fasting/schedule/">Intermittent fasting schedule and planner</a></li>
  <li><a href="/intermittent-fasting/weight-loss/">Intermittent fasting for weight loss</a></li>
  <li><a href="/intermittent-fasting/walking-while-fasting/">Walking while fasting</a></li>
  <li><a href="/intermittent-fasting/apps/">How to choose a fasting app</a></li>
</ul>
<h2>Sources</h2>
<ul class="sources"><li><a href="{SRC_HOPKINS[1]}">{SRC_HOPKINS[0]}</a></li><li><a href="{SRC_MAYO[1]}">{SRC_MAYO[0]}</a></li></ul>
{cta_band('intermittent-fasting')}
"""


def schedule_body():
    return f"""
<p class="answer">Pick the time you want to start eating, and a fasting length. The planner shows the eating window and
when to stop. Many daily plans use an eating window of about six to eight hours; choose a pattern you can keep.</p>
{SAFETY_NOTE}

<section class="tool" data-tool="fasting-planner">
  <h2>Fasting window planner</h2>
  <form>
    <fieldset class="radios">
      <legend>I know my...</legend>
      <label><input type="radio" name="mode" value="first" checked> first meal time</label>
      <label><input type="radio" name="mode" value="last"> last meal time</label>
    </fieldset>
    <div class="row">
      <label class="field"><span>Time</span><input type="time" name="time" value="12:00"></label>
      <label class="field"><span>Fast for</span>
        <select name="fast">
          <option value="12">12 hours</option><option value="13">13 hours</option><option value="14">14 hours</option>
          <option value="15">15 hours</option><option value="16" selected>16 hours (16/8)</option>
        </select></label>
    </div>
  </form>
  <div class="result" aria-live="polite"></div>
  <p class="meta">The planner is plain time arithmetic. It does not tell you what's right for your body.</p>
</section>

<h2>Example 16/8 schedules</h2>
<div class="tablewrap"><table>
<thead><tr><th>First meal</th><th>Last meal</th><th>Fast</th></tr></thead>
<tbody>
<tr><td>10:00 AM</td><td>6:00 PM</td><td>6:00 PM to 10:00 AM</td></tr>
<tr><td>12:00 PM</td><td>8:00 PM</td><td>8:00 PM to 12:00 PM</td></tr>
<tr><td>1:00 PM</td><td>9:00 PM</td><td>9:00 PM to 1:00 PM</td></tr>
</tbody></table></div>

<h2>Choosing a window you can keep</h2>
<ul>
  <li>Work backwards from your day: when do you usually eat with other people, and when do you train or walk?</li>
  <li>If 16 hours sounds like a lot, a shorter fast is a reasonable place to start. Ask your doctor if you're unsure.</li>
  <li>Longer is not better. Fasts of 24 hours or more may be dangerous, according to Johns Hopkins Medicine.</li>
  <li>Drinking water is fine; what counts as breaking a fast depends on the plan you follow.</li>
</ul>
<p>Looking for the walking side? See <a href="/intermittent-fasting/walking-while-fasting/">walking while fasting</a>.</p>
<h2>Sources</h2>
<ul class="sources"><li><a href="{SRC_HOPKINS[1]}">{SRC_HOPKINS[0]}</a></li></ul>
{cta_band('intermittent-fasting-schedule')}
"""


def fasting_weight_body():
    return f"""
<p class="answer">Intermittent fasting can help some people eat less, and research suggests it works about as well as a
typical low-calorie diet. It isn't magic, it isn't necessary, and it isn't for everyone.</p>
{SAFETY_NOTE}

<h2>What the evidence says</h2>
<ul>
  <li><strong>Comparable to other diets.</strong> Mayo Clinic: "Research suggests that alternate-day fasting is about as effective as a typical low-calorie diet for weight loss."</li>
  <li><strong>Calories still matter.</strong> Mayo Clinic: eating fewer calories than you expend remains the basis for losing weight.</li>
  <li><strong>Long-term effects are unclear.</strong> There is little long-term research, so long-term benefits and risks are unknown.</li>
  <li><strong>Some studies show weight loss.</strong> Johns Hopkins Medicine cites small studies in which adults with obesity lost weight, and advises checking with a doctor first.</li>
</ul>

<h2>What to expect</h2>
<p>Hunger, tiredness and headaches are common side effects, and Mayo Clinic notes most go away within a month. Watch the
trend of your weight over weeks rather than any single weigh-in, since day-to-day readings move around.</p>

<h2>Where walking fits</h2>
<p>Fasting changes when you eat. Walking changes how much you move. They are separate levers and you can use either
without the other. StepFast tracks both so you can see what's happening. Read
<a href="/walking-for-weight-loss/">walking for weight loss</a> or
<a href="/intermittent-fasting/walking-while-fasting/">walking while fasting</a>.</p>
<h2>Sources</h2>
<ul class="sources"><li><a href="{SRC_MAYO[1]}">{SRC_MAYO[0]}</a></li><li><a href="{SRC_HOPKINS[1]}">{SRC_HOPKINS[0]}</a></li></ul>
{cta_band('intermittent-fasting-weight-loss')}
"""


def walking_fasting_body():
    return f"""
<p class="answer"><strong>Does walking break a fast?</strong> No. Walking uses energy but doesn't add any food or drink
calories, so it doesn't end a fast.</p>
{SAFETY_NOTE}

<h2>Walking while fasting: practical points</h2>
<ul>
  <li><strong>Go easy at first.</strong> A relaxed walk is different from a hard workout. If you feel dizzy, faint or unwell, stop, sit down and eat.</li>
  <li><strong>Athletes may struggle to fuel.</strong> Mayo Clinic notes that athletes can find it hard to fuel properly while fasting.</li>
  <li><strong>If you have diabetes or take medication,</strong> talk to your doctor first. Johns Hopkins Medicine raises a concern about unsafe low blood sugar during fasting.</li>
  <li><strong>Walking after you eat is fine too.</strong> The timing is about what suits you.</li>
</ul>

<h2>How StepFast handles it</h2>
<p>StepFast compares your steps with your daily goal. When you're short, it leads with walking: at
{C.WALK_STEPS_PER_MIN} steps a minute, every 1,000 steps is about {1000 // C.WALK_STEPS_PER_MIN} minutes. On days you can't
walk, and only if fasting is on for you, it can suggest a later first meal instead (about
{C.LATER_BREAKFAST_MIN_PER_1000} minutes per 1,000 steps), never beyond {C.FAST_CAP_HOURS} hours of total fasting.
<a href="/how-it-works/">See how it works</a>.</p>
<h2>Sources</h2>
<ul class="sources"><li><a href="{SRC_HOPKINS[1]}">{SRC_HOPKINS[0]}</a></li><li><a href="{SRC_MAYO[1]}">{SRC_MAYO[0]}</a></li></ul>
{cta_band('intermittent-fasting-walking-while-fasting')}
"""


def apps_body():
    return f"""
<p class="answer">A good fasting app keeps the timer simple, tells you the real price up front, screens for who shouldn't
fast, and doesn't need an account you don't want. Use the checklist below on any app, including StepFast.</p>

<h2>A checklist for choosing</h2>
<div class="tablewrap"><table>
<thead><tr><th>Question to ask</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Is the basic timer free?</td><td>Some apps lock custom fasting windows behind a subscription.</td></tr>
<tr><td>What does it cost after any trial or discount?</td><td>Check the renewal price on the App Store page before you start.</td></tr>
<tr><td>Does it screen for who shouldn't fast?</td><td>Fasting isn't right for everyone, and good apps say so.</td></tr>
<tr><td>Does it need an account?</td><td>Some apps store data on a server, others only on your phone.</td></tr>
<tr><td>Can you turn off streaks and notifications?</td><td>Pressure to extend a fast isn't helpful.</td></tr>
<tr><td>Does it work with Apple Health?</td><td>Useful if you want steps and weight in one place.</td></tr>
</tbody></table></div>

<h2>Where StepFast fits</h2>
<p>StepFast is a walking-first weight tracker for iPhone, with a fasting timer as an option. It suits you if you want
steps, weight and an optional fasting window in one simple app, with no account. It is not a calorie or food logger, it
is iPhone only, and the interface is in English. The App Store listing shows which features are free and which are in the
optional paid tier.</p>

<h2>Other apps you may come across</h2>
<p>Well-known fasting apps include Zero, Simple, Fastic, BodyFast and Life Fasting Tracker. Prices and features change,
so compare each one's current App Store page using the checklist above.</p>
{SAFETY_NOTE}
{cta_band('intermittent-fasting-apps')}
"""


def walking_body():
    return f"""
<p class="answer"><strong>How many steps a day to lose weight?</strong> There is no single number that works for everyone.
Steps measure how much you move, while your weight also depends on what you eat and other factors. Build up gradually
and watch your weight trend over weeks.</p>

<h2>Walking is a good place to start</h2>
<p>The CDC says adults need 150 minutes of moderate-intensity physical activity a week, plus at least two days of
muscle-strengthening activity. Fast walking is one of the moderate-intensity activities it lists. A moderate pace is one
where you can talk but not sing.</p>

<h2>Pick a step goal and ramp up</h2>
<p>If you walk 3,000 steps a day now, jumping to 10,000 tomorrow is a lot. A steady increase each week is easier to keep.
Use the <a href="/tools/step-goal/">step goal planner</a> to pace it.</p>

<h2>"I walk but the scale is stuck"</h2>
<ul>
  <li>Daily weight moves around, so look at the trend over several weeks.</li>
  <li>Weight depends on food as well as movement. Calories in versus calories out remains the basis (Mayo Clinic).</li>
  <li>Walking has benefits that don't show up on a scale. Judge it by whether you can keep doing it.</li>
  <li>If you're worried, or have a medical condition, speak with a clinician.</li>
</ul>

<h2>Where fasting fits</h2>
<p>Fasting is optional. Some people add it, many don't. Read
<a href="/intermittent-fasting/">about intermittent fasting</a> and <a href="/safety/">who should skip it</a>.</p>

<h2>How StepFast helps</h2>
<p>StepFast shows today's steps against your goal in four zones, lets you log your weight, and shows trends over time. It
suggests a walk when you're short on steps. <a href="/how-it-works/">See how it works</a>.</p>
<h2>More walking questions</h2>
<ul>
  <li><a href="/walking-10000-steps-weight-loss/">Will 10,000 steps a day help you lose weight?</a></li>
  <li><a href="/how-long-to-walk-for-weight-loss/">How long should you walk for weight loss?</a></li>
  <li><a href="/tools/step-goal/">Build a gradual step goal from your current average</a>.</li>
</ul>
<h2>Sources</h2>
<ul class="sources"><li><a href="{SRC_CDC_ADULT[1]}">{SRC_CDC_ADULT[0]}</a></li><li><a href="{SRC_CDC_COUNTS[1]}">{SRC_CDC_COUNTS[0]}</a></li><li><a href="{SRC_MAYO[1]}">{SRC_MAYO[0]}</a></li></ul>
{cta_band('walking-for-weight-loss')}
"""


def ten_thousand_steps_body():
    return f"""
<p class="answer"><strong>Will 10,000 steps a day help you lose weight?</strong> It can be one way to add movement, but 10,000 steps is not a required target and cannot predict how much weight one person will lose. A useful goal depends on your starting point, health and routine.</p>

<h2>Is 10,000 steps a day necessary?</h2>
<p>No. The CDC's adult activity guidance is based on minutes of activity, including at least 150 minutes of moderate-intensity activity each week for substantial health benefits. It does not set 10,000 steps as a universal weight-loss prescription. Some activity is better than none, and the guidance can be spread across the week.</p>

<h2>What if you are walking 10,000 steps but the scale is not changing?</h2>
<p>Steps alone cannot explain a change in body weight. Weight management can involve both physical activity and eating patterns, and a step total does not show what any one person's weight should do or when it should change. A single weigh-in also cannot show a longer-term trend. If you are concerned about your weight trend or have a health condition, ask a health professional for advice that fits your situation.</p>

<h2>Choose a goal from your own baseline</h2>
<ol>
  <li>Look at a normal week of steps, if you have a step history.</li>
  <li>Choose an increase that feels manageable and repeat it before raising the target again.</li>
  <li>Pay attention to comfort and consistency. Reduce the goal if it causes pain or does not fit your routine.</li>
</ol>
<p>If you want help pacing a step increase, use the <a href="/tools/step-goal/">Step goal planner</a>. It creates a gradual step schedule; it does not estimate pounds lost. Read the broader <a href="/walking-for-weight-loss/">walking and weight guide</a> for step-count context.</p>

<h2>What 10,000 steps can tell you</h2>
<p>A step total can help you notice how much you moved that day. It cannot tell you whether you reached a personal weight goal. StepFast tracks steps and weight trends, but it does not turn a step count into a promised weight change.</p>

<h2>Common questions</h2>
{faq([
    ("Do I need 10,000 steps to lose weight?", "No. It is not a required number for everyone. Choose activity that fits your starting point and health."),
    ("How much weight will I lose by walking 10,000 steps a day?", "There is no reliable amount that can be calculated from steps alone. Your weight response depends on more than a step count."),
    ("Should I go from 4,000 steps straight to 10,000?", "You do not have to make that jump. Start from your usual activity and build at a pace you can maintain."),
    ("What if I walk 10,000 steps and my weight stays the same?", "Look at the longer-term pattern and consider other factors that affect weight. A clinician can help if you have concerns."),
])}

<h2>Sources</h2>
<ul class="sources">
  <li><a href="{SRC_CDC_ADULT[1]}">{SRC_CDC_ADULT[0]}</a></li>
  <li><a href="https://www.niddk.nih.gov/health-information/weight-management/adult-overweight-obesity/treatment">NIDDK: Treatment for Overweight &amp; Obesity</a></li>
</ul>
<p class="meta">This page is general wellness information, not a personal weight-loss plan or medical advice.</p>
{cta_band('walking-10000-steps-weight-loss')}
"""


def walking_duration_body():
    return f"""
<p class="answer"><strong>How long should you walk each day for weight loss?</strong> There is no fixed number of minutes that guarantees weight loss. For general health, CDC guidance for adults is at least 150 minutes of moderate-intensity activity each week; brisk walking counts. That could be 30 minutes on five days, or shorter sessions spread across the week.</p>

<h2>Use the weekly guideline as a reference, not a promise</h2>
<p>The 150-minute recommendation is a general physical-activity guideline, not a weight-loss dose. The CDC says adults can spread activity through the week and break it into smaller chunks. Some activity is better than none. If you are inactive, start with an amount that feels manageable and build gradually.</p>

<div class="card">
  <h3>One way to organize 150 minutes</h3>
  <p>Walk briskly for about 30 minutes on five days of the week. If a longer walk does not fit, split the time into shorter walks. A moderate pace is one where you can talk but not sing.</p>
  <p class="meta">This is an example based on CDC general guidance, not a personalized prescription.</p>
</div>

<h2>What counts as a brisk, moderate walk?</h2>
<p>Use the talk test: at a moderate pace, you can talk but not sing. Pace and ability vary. You can begin more gently, take breaks, and increase duration as your body and schedule allow. Stop and seek medical advice if activity causes concerning symptoms.</p>

<h2>Why walking time cannot predict weight loss</h2>
<p>Minutes walked do not translate into a guaranteed amount of weight change. NIDDK describes weight management as involving both eating patterns and physical activity. A walking routine can support activity goals, but a particular number of minutes cannot say how much weight you will lose or how quickly.</p>

<h2>Make a routine you can repeat</h2>
<ul>
  <li>Pick days and times that fit a normal week.</li>
  <li>Start with shorter walks if that is what you can do consistently.</li>
  <li>Track your steps and weight over time rather than judging the plan from one day.</li>
</ul>
<p>For step-based pacing, try the <a href="/tools/step-goal/">Step goal planner</a>. For a step-count answer, see <a href="/walking-10000-steps-weight-loss/">what 10,000 steps can and cannot tell you</a>.</p>

<h2>Common questions</h2>
{faq([
    ("Is 30 minutes of walking a day enough?", "Thirty minutes on five days is one way to reach the CDC's 150-minute weekly activity recommendation for adults. It is a general health guideline and does not guarantee weight loss."),
    ("Can I split my walk into shorter sessions?", "Yes. CDC guidance says activity can be spread through the week and broken into smaller chunks."),
    ("Do I need to walk every day?", "No. The weekly guideline can be spread across different days. Choose a schedule that works for you."),
    ("How fast should I walk?", "A moderate pace is one where you can talk but not sing. Adjust the pace to your ability."),
])}

<h2>Sources</h2>
<ul class="sources">
  <li><a href="{SRC_CDC_ADULT[1]}">{SRC_CDC_ADULT[0]}</a></li>
  <li><a href="{SRC_CDC_COUNTS[1]}">{SRC_CDC_COUNTS[0]}</a></li>
  <li><a href="https://www.niddk.nih.gov/health-information/weight-management/adult-overweight-obesity/treatment">NIDDK: Treatment for Overweight &amp; Obesity</a></li>
</ul>
<p class="meta">This page is general wellness information, not a personal exercise or weight-loss prescription.</p>
{cta_band('how-long-to-walk-for-weight-loss')}
"""


def step_goal_body():
    return f"""
<p class="answer">Enter the steps you average now and a target. The planner builds a week-by-week ramp so you add a
little at a time. It is a pacing plan, not a weight prediction.</p>

<section class="tool" data-tool="step-goal">
  <h2>Step goal planner</h2>
  <form>
    <div class="row">
      <label class="field"><span>Your average steps a day now</span><input type="number" name="current" inputmode="numeric" min="0" max="40000" value="3000"></label>
      <label class="field"><span>Your target (steps a day)</span><input type="number" name="goal" inputmode="numeric" min="1" max="40000" value="7000"></label>
      <label class="field"><span>Add each week</span>
        <select name="inc"><option value="250">250 steps</option><option value="500" selected>500 steps</option><option value="1000">1,000 steps</option></select></label>
    </div>
  </form>
  <div class="result" aria-live="polite"></div>
</section>

<h2>How to use it</h2>
<ul>
  <li>Find your current average in the Health app or any step counter, over a normal week.</li>
  <li>Choose a small weekly increase you can keep. Skipping a week or staying put is fine.</li>
  <li>Stop and talk to a clinician if walking causes pain, dizziness or chest discomfort.</li>
</ul>
<p>The CDC's guideline for adults is 150 minutes of moderate-intensity activity a week
(<a href="{SRC_CDC_ADULT[1]}">CDC</a>). Steps and minutes are two ways of looking at the same habit. StepFast tracks your steps
and shows them against a daily goal; <a href="/how-it-works/">see how it works</a>.</p>
{cta_band('tools-step-goal')}
"""


PAGES = [
    dict(slug="", title="StepFast: Walking & Weight Loss Tracker for iPhone",
         description="Track your steps and weight with StepFast, an iPhone app for adults. Follow a walking-first plan, add optional fasting, and keep your data on your phone.",
         h1=None, kind="home", body=home_body, nav=None),
    dict(slug="how-it-works", title="How StepFast Works: Steps, Weight and Optional Fasting",
         description="See how StepFast turns your daily steps into a simple plan: goal zones, a step-gap calculator, an optional fasting timer and safety checks.",
         h1="How StepFast works", kind="page", body=how_body, nav="how-it-works"),
    dict(slug="weight-tracking", title="Weight Tracker App for iPhone: See Weight Trends | StepFast",
         description="Track weight over time with StepFast. Learn how to choose a weigh-in routine, understand daily changes, and use a trend without chasing one number.",
         h1="Track your weight over time, not one weigh-in at a time", kind="article", body=weight_tracking_body,
         nav=None, published="2026-10-30", modified="2026-10-30"),
    dict(slug="safety", title="Safety and Who Shouldn't Fast | StepFast",
         description="Who should not fast, what StepFast's safety check does, and when to stop and get help. StepFast is a wellness app, not medical advice.",
         h1="Safety and who shouldn't fast", kind="article", body=safety_body, nav="safety"),
    dict(slug="intermittent-fasting", title="What Is Intermittent Fasting? Who Should Skip It | StepFast",
         description="A plain-language guide to intermittent fasting: common patterns, what research suggests, side effects, who should skip it, and how StepFast keeps it optional.",
         h1="Intermittent fasting: what it is and who it's not for", kind="article", body=fasting_pillar_body, nav="intermittent-fasting"),
    dict(slug="intermittent-fasting/schedule", title="Intermittent Fasting Schedule and 16:8 Planner | StepFast",
         description="Plan an intermittent fasting window with a free planner. Enter a first or last meal time and a fasting length to see your eating window.",
         h1="Intermittent fasting schedule and planner", kind="article", body=schedule_body, nav="intermittent-fasting"),
    dict(slug="intermittent-fasting/weight-loss", title="Intermittent Fasting for Weight Loss: The Evidence | StepFast",
         description="What Mayo Clinic and Johns Hopkins say about intermittent fasting and weight loss, what to expect, and where walking fits in.",
         h1="Intermittent fasting for weight loss: what the evidence says", kind="article", body=fasting_weight_body, nav="intermittent-fasting"),
    dict(slug="intermittent-fasting/walking-while-fasting", title="Does Walking Break a Fast? Walking While Fasting | StepFast",
         description="Walking doesn't break a fast. Practical points for walking while fasting, who should be careful, and how StepFast handles step gaps.",
         h1="Does walking break a fast?", kind="article", body=walking_fasting_body, nav="intermittent-fasting"),
    dict(slug="intermittent-fasting/apps", title="How to Choose an Intermittent Fasting App | StepFast",
         description="A checklist for choosing a fasting app: free timer, clear pricing, safety screening, accounts, and Apple Health, plus where StepFast fits.",
         h1="How to choose an intermittent fasting app", kind="article", body=apps_body, nav="intermittent-fasting"),
    dict(slug="walking-for-weight-loss", title="Walking for Weight Loss: How Many Steps a Day? | StepFast",
         description="How many steps a day to lose weight? There is no one number. How to ramp up gradually, what the CDC recommends, and what to do when the scale is stuck.",
         h1="Walking for weight loss: how many steps a day?", kind="article", body=walking_body, nav="walking-for-weight-loss"),
    dict(slug="walking-10000-steps-weight-loss", title="10,000 Steps a Day for Weight Loss: What to Expect | StepFast",
         description="Can 10,000 steps a day help with weight loss? Learn what the number can and can't tell you, how to build from your baseline, and why it cannot predict a result.",
         h1="Will 10,000 steps a day help you lose weight?", kind="article", body=ten_thousand_steps_body,
         nav="walking-for-weight-loss", published="2026-10-30", modified="2026-10-30"),
    dict(slug="how-long-to-walk-for-weight-loss", title="How Long Should You Walk for Weight Loss? | StepFast",
         description="How long should you walk each day? See the CDC's general weekly activity guidance, ways to split up walks, and why minutes cannot promise weight loss.",
         h1="How long should you walk each day for weight loss?", kind="article", body=walking_duration_body,
         nav="walking-for-weight-loss", published="2026-10-30", modified="2026-10-30"),
    dict(slug="tools/step-goal", title="Step Goal Planner: Build a Weekly Walking Ramp | StepFast",
         description="Free step goal planner. Enter your current steps and a target, and get a week-by-week plan that adds a little at a time.",
         h1="Step goal planner", kind="article", body=step_goal_body, nav="walking-for-weight-loss"),
]

