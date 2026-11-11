# Portfolio experience plan (Phase 3)

Nov 6, 2026 · @Shaurya Nigam

## What's decided

This plan turns the Phase 2 concept into a page-by-page blueprint. Nothing here is code yet; it's what Phase 4 builds from.

| Decision | Choice |
| --- | --- |
| Concept | **The Set + Booth Lights**: the site is laid out like a DJ set, opens with a zoom into a four-CDJ booth, and has a light/dark switch that turns daylight mode into club mode |
| The booth | 4 CDJ-style players, 1 mixer in the middle, built from code in Blender (v3 render is the baseline; you'll refine it) |
| Visual direction | Afterhours (dark) + Daylight Studio (light). Final colours picked once you see them in the real UI |
| Design rules | Apple-level restraint, Lando/Dennis-level motion, the Apple design skill as the motion and interaction rulebook |
| Gamification v1 | Achievements with popups, energy meter, pit-stop game, penalty game, Ctrl+K command palette (details in Gamification v1) |
| Out | Keyboard instrument |
| Budget | Zero: free tools, free tiers, models built from code |
| Non-negotiables | Content one click away, nav always visible, fast on phones, sound on by default with a mute always in view, reduced-motion version |

## Site map and visitor paths

The whole portfolio is **one long scrolling page** played like a set, plus a few separate pages (each project's full case study, resume, and the hidden page). There are three kinds of visitor, and each needs its own path.

&#91;embedded content: the set · 8 sections in scroll order, with two game interludes\]

**1. The recruiter (30 seconds, no patience)**

- Name, role and one "Drop in?" button are readable in the first screen, before the booth zoom even starts. That button replaces both the old "View projects" button and the "Skip intro" pill.
- Nav (Experience, Projects, Certifications, Leadership, Contact, a highlighted Resume button, and a small game controller icon that opens both games) is visible at all times. One click jumps straight to that section and skips the animation.
- The Resume link opens a PDF in a new tab. The Contact section has email, LinkedIn and GitHub as plain links.

**2. The explorer (has time, wants the show)**

- Scrolls the whole set: booth zoom, intro, experience, the drop, tracklist, certifications and leadership, encore, with two game interludes along the way.
- Finds achievements, fills the energy meter, plays the games, flips the Booth Lights switch.

**3. Phone visitors (likely the majority from a resume link)**

- No 3D. The booth shows as a lightweight still or short rendered clip, and the page goes straight into content.
- Games get touch controls. The command palette becomes a menu button.

## Storyboard, section by section

Each section lists what the visitor sees, what scrolling and hovering do, and the phone or reduced-motion version.

### 0. Loader: F1 start lights

- Five red lights come on one by one while the page actually loads. That's about 1.5 to 2 seconds on a good connection.
- **When loading and the lights don't finish together:**
  - *Site loads before the lights finish:* the lights always play their full sequence at normal pace (about 1.5 seconds, one light every 300 ms). Then the start button appears and waits for the visitor. Nothing happens until they click, tap or press Enter or Space.
  - *Lights would finish before the site has loaded:* the first four lights track real loading progress, and the fifth only comes on once everything needed for the opening is ready. While it waits, the fifth light pulses softly. After about 3 seconds a small line appears under it with the real percentage ("Warming up the tyres · 82%"), so it never looks frozen.
  - *Very slow connection (over about 8 seconds):* a "Drop in now" link appears. It starts the site with a lighter opening (a still image of the booth instead of the zoom frames, which keep loading in the background).
- **The start button (this is what turns the sound on).** Once all five are lit, a single prompt appears under them: **"Lights out"**, with a small hint "click, tap or press Space". Pressing it is the visitor's first click, so the browser lets the sound start. On that same frame the lights go out, the engine-to-bass sound hits and the site launches. A tiny "enter without sound" link sits underneath for people at work.
- No auto-enter: the site waits on the start screen until the visitor presses. The lights stay lit and the button breathes gently so it's obvious what to do.
- Skipped on repeat visits within a session (sound then starts on the first click anywhere).
- **Reduced motion:** the lights fade in together, then fade out, with the same button.

### 1. Booth zoom (the opening)

- **First screen:** the four-CDJ booth in the dark, lit softly, with your name, role line "Full-Stack AI Engineer · Voice Agents · RAG · ML", a smaller tagline under it (working version: "I build AI that listens, talks and gets things done. Tested end to end."), and two buttons over the top: Drop in? (the main one) and Resume. Nav is visible.
- **On scroll:** nothing moves until the visitor scrolls. The zoom is tied to the scroll position, so it goes exactly as far as they scroll and reverses if they scroll back up. Over two to three scroll lengths the camera glides from the full booth into one CDJ, and that CDJ settles into a close, slightly angled shot with the whole deck still in frame (screen, jog wheel and buttons). It never zooms so far that the screen fills the viewport. Scrolling on from there plays the Lando-style transition into the Intro. A real song is playing on that CDJ: its title and waveform are on the screen, the playhead moves in time with the audio, and the jog wheel's ring turns with it. You're now "inside the set". This uses the Apple technique: pre-rendered frames from the Blender script, played in step with the scroll.
- **The song:** it has to be a track we're allowed to use, because a commercial EDM release would get the site flagged for copyright. Free options: a royalty-free EDM track (for example from Pixabay Music, free with no attribution needed), a Creative Commons track with credit in the footer, or a track you or a friend produced. You pick it, and the CDJ screen and waveform are generated from that exact file.
- A **Skip intro** is now the Drop in? button. Tapping it plays the whole booth zoom for you at speed (about 1.2 seconds, with a quick whoosh as the track speeds up), settles on that same close shot of the CDJ, then a Lando-style transition reveals the Intro. One tap and the main content is in front of them, and they still get the wow moment. Reduced motion: a quick fade straight to the Intro.
- **Phone:** no booth at all. Phones go straight from the loader to the Intro (name, role line, tagline, Drop in? becomes a simple "See my work" scroll, plus Resume). The booth images are never downloaded on phones, so the site loads much faster on mobile data. The DJ feel stays in the small details: the waveform scroll bar, the accent colour and the sounds.
- **Reduced motion:** a still image with a cross-fade into the Intro.

**Agreed (10 Nov): the booth as a four-deck hub.** Your idea, approved as below:

- **First visit is unchanged.** Scrolling dives into Deck 1 (left of the mixer) and plays the full set from the Intro onwards. Drop in? does the same. Recruiters never need to know the other decks exist.
- **Scrolling back up past the Intro zooms back out to the booth.** It's the same scroll-scrub in reverse, so no new trick is needed. A small booth icon in the nav (and the Esc key) also takes you back.
- **At the booth, you pick a deck.** Use the left and right arrow keys, the 1 to 4 keys, a sideways trackpad swipe, or hover/click. The picked deck lights up and its screen shows its "track": `02 · EXPERIENCE`, `03 · PROJECTS`, `04 · PIT LANE`, with a waveform. Scroll down or press Enter to dive into it.
- **Deck line-up:** Deck 1 is the full set, Deck 2 is Experience, Deck 3 is Projects (The Drop and Tracklist), and Deck 4 is Games (Pit stop and Penalty shootout). **The mixer is Contact and Resume**, the "master channel" in the middle.
- **Diving into Decks 2 to 4 lands you at that section on the same page,** so the racing line still shows where you are and you can keep scrolling through the rest of the site.
- **How we keep it light:** only Deck 1 gets the full frame-by-frame scroll zoom. The other three get a short pre-rendered dive clip (about 1 second) that loads quietly after the site is ready. The same Blender script exports all four camera paths.
- **A hint for curious visitors:** the first time someone zooms back out, a small line appears under the booth: "← → to pick a deck."
- **Gamification:** dropping into all four decks unlocks a **"Back to back"** achievement (DJ slang for two DJs sharing decks) and adds to the energy meter.
- **Phones:** unchanged. There's no booth on phones, so the nav and the game controller icon cover these shortcuts.

### 2. Intro (who you are)

- Big, calm type in the Apple style: one strong line about what you build, a short paragraph, a photo or portrait treatment, and three quick facts (for example the AWS certifications, the AutoMinds internship, your university).
- **Interest chips:** a small line "Into F1 · football · EDM". Tapping F1 opens Pit stop, football opens Penalty shootout (both in an overlay with instant restart and a close button), and EDM plays a few seconds of the booth track. This is where most visitors first find the games.
- Lines of text slide up and fade in as they enter, Lando-style.

### 3. Experience (work and education)

On the site these use plain names, so a recruiter scanning the nav finds them at once. The DJ theme stays in how they look, not in what they're called.

- **Experience.** One role card per job, newest first. AutoMinds LLC, Voice Agent Intern, Jun to Jul 2026, remote (Texas, USA): the four resume bullets, a small stats strip (278 scenarios · 200+ graded calls · \~90 bugs · 90% fixed) and a "How I tested it" button that expands the card in place. The expanded card tells the testing framework story in words only: the problem (a voice receptionist that could confirm bookings that never happened), how your framework caught it (generated test scenarios, graded calls, bug reports), a simple diagram we draw ourselves, and the results. It's company work, so no code, real screens or repo link, and it is not listed in the Tracklist. Education sits under it as one line: Bennett University, B.E. CSE (AI specialisation), CGPA 8.88, 2024 to 2028.

**Interlude: "Quick pit stop?"** A slim strip between Experience and The Drop where Pit stop is playable right there in the page, with your best time shown. Scrolling past skips it, and it never blocks the content.

### 4. The Drop (featured project)

- The music "drops" here: the one big Igloo-style moment, and it belongs to **SARAH**, your flagship. Particles morph from the waveform into SARAH's three-stage pipeline (prepare, live loop, score), then settle into a full-width case-study card.
- The card holds a muted screen recording of a voice interview, the hook line ("A voice agent that can't score anything the candidate didn't actually say"), and three headline numbers: 97.3% of judge verdicts named a real missing element, 56/56 scores backed by verified quotes, and κ = 0.731 agreement with a human rater.
- One small interactive touch: a replay of the real interview excerpt, where each follow-up highlights the candidate's quoted words as the judge "verifies" them.
- **Phone and reduced motion:** the particle morph is replaced by a simple fade-in of the card.

### 5. Tracklist (all projects)

- Projects are listed like a DJ's tracklist in two parts:
  - **Released:** SARAH, PITWALL (F1 strategy, with a live demo), CivicFix, NABHA Telemedicine. Each row shows number, title, stack and one key stat.
  - **Unreleased IDs** (DJ slang for tracks that aren't out yet): ZEN AI and TerraLens, each with a clear "In progress" badge, what's built so far, and what's next.
- **Hover** expands a row (the expand-on-hover you liked): a video or screenshot slides in with a two-line summary and links.
- **Click** opens the full case-study page, with a smooth shared transition from the row.
- Filter chips (Voice AI, LLM evaluation, NLP, full-stack) re-sort the list with a quick animation.

**Interlude: "Half-time".** The same kind of strip between Tracklist and Certifications, with Penalty shootout playable in place and your score shown. Scrolling past skips it. On phones, both interludes show a Play button that opens the game full screen with touch controls.

### 6. Certifications, leadership and skills

- **Certifications.** Styled as backstage passes on lanyards, one per certificate, each with a Verify link that opens the real credential: AWS Certified Solutions Architect – Associate (2026 to 2029), AWS Certified AI Practitioner (2026 to 2029), and NPTEL (IIT Kanpur) Soft Skills and Personality, Elite + Gold, Top 1%. Hover tilts the pass slightly, like it's hanging. Phone and reduced motion: flat cards.
- **Leadership.** One card per role.
  - GeeksforGeeks Student Chapter, Bennett: Multimedia Head (Senior Core), Aug 2025 to May 2026. Secured Casio India sponsorship for GeekCode events (500+ registrations beyond campus) and led 10+ reels with 50K+ total views. A muted reel can play in the card on hover.
  - CodeChef Student Chapter, Bennett: Social Media Manager, Aug 2024 to May 2025. Organised and ran coding contests and workshops (250+ participants) and designed and scheduled 10+ posts a month across Instagram and LinkedIn.
- **Skills.** A compact strip grouped like mixer channels: AI/ML and LLM evaluation, voice agents, full-stack, cloud. Each channel's level meter fills as you scroll past, and hovering a skill highlights the projects above that use it.

### 7. Encore (contact)

- **A proper Contact section**, laid out in four parts:
  1. **Headline and status.** A big line ("Let's build something"), then one line on what you're open to (for example AI and voice-agent internships), with a small green "Available" dot, your location and time zone (Delhi NCR, India · IST, open to remote), and "I usually reply within a day :)".
  2. **Email, three ways.** A large "Email me" button that opens a ready-to-write email with the subject already filled in ("Hi Shaurya, from your portfolio"). The button has a small menu: Open in Gmail (opens Gmail's compose window in the browser), Open in Outlook, Use my mail app, or Copy address (with a "Copied" popup). This matters because a plain email link does nothing for people on a laptop with no mail app set up, which is very common.
  3. **A short message form.** Name, email and message, sent straight to your inbox without the visitor leaving the site. It uses a free service (Resend or Formspree free tier), has hidden spam protection, and shows a friendly "Sent" confirmation. This catches people who won't open their own email.
  4. **Link buttons.** LinkedIn, GitHub and Resume (download the PDF), each with an icon, opening in a new tab. Optionally a "Book a 15-min call" link through Cal.com's free plan.
- **Small touches (Dennis Snellenberg / Lando style):**
  - A live local clock beside the status ("It's 3:14 PM for me in India!"), so international recruiters know when you'll reply.
  - A magnetic "Email me" button that leans toward the cursor and springs back.
  - Quick-pick chips at the top of the form (Internship, Project, Just saying hi) that fill in the subject line, so a message takes seconds to write.
- **Left out on purpose:** your phone number. It's on your resume, but on a public site it attracts spam calls.
- **Everywhere else:** the footer on every page repeats the email and the three icons, and Ctrl+K has "Copy email" and "Email Shaurya", so contact is never more than one click away.
- The waveform scroll bar reaches the end of the track here, which counts as an achievement.
- A small footer holds credits and the achievements counter.

### Extra touches borrowed from your favourite sites (all go in the first build; we keep what works)

- **Section markers on the racing line (replaces the marquee).** The racing line marks each section like a corner on a circuit ("T3 · Tracklist"), and the section names travel along the line at a speed that follows your scroll. **Track change note:** when a section starts, the mini player flips to "Now playing: Experience" for a moment, like a CDJ loading the next track. If the racing line doesn't make the final build, the cue point divider ("CUE 03 · TRACKLIST") takes its place.
- **Page transitions (modelled on Lando's, your favourite).** Opening a case study wipes a dark panel across the screen with the project's name on it, then reveals the new page. Going back plays it in reverse.
- **Numbers that count up (Apple).** Every stat (278 scenarios, 214,993 laps, 50K+ views) counts up from zero the first time it scrolls into view.
- **Giant signature footer (Lando).** At the very bottom, your name in huge type is revealed as the last part of the page scrolls up, like closing credits.
- **A playful 404 page (Henry Heffernan's spirit).** A CDJ screen reading "Track not found", with the jog wheel spinning on nothing and one button: back to the set. Finding it unlocks a hidden achievement.
- **Racing line through the page.** A thin line shaped like an F1 circuit draws itself down the page as you scroll, linking the sections like corners on a track. We judge it in the real build and drop it if it looks busy.
- **Sticky story (Apple product pages).** In case studies, a visual stays pinned while the text beside it changes. Example: PITWALL's strategy chart builds step by step as you read.
- **Line-by-line headings (Lando, Apple).** Big headings rise into place one line at a time from behind a mask.
- **Spotlight cards.** A soft light follows the cursor across cards, like a booth light sweeping over them. The cursor itself will be custom (never the default white arrow); its exact design is decided later.
- **A few magnetic buttons.** Only the key buttons (Drop in?, Resume, the main contact button) lean towards the cursor. Everything else stays still. We try other hover styles for the rest during the build.
- **Next race countdown.** A tiny widget, "Next race: Abu Dhabi GP in 4 days", from a free F1 data source.
- **Now listening.** Shows what you're playing on Spotify right now, or the last track you played, via the free Spotify API. You connect your Spotify account once during the build.
- **Sign the setlist.** Visitors leave a name and a one-line message on a small wall. Built with Supabase. Messages appear straight away. A basic spam filter stops bots, and you can delete any message yourself from a simple private page.
- **Theme follows the visitor's device.** Dark or light mode matches the visitor's system setting by default, and the Booth Lights switch can change it.
- Not doing: film grain, the card-to-full-screen video and the sideways crate.

### Toolkit: what we take from each library (your list, 10 Nov)

All free for a portfolio. React Bits is MIT + Commons Clause (free to use, just not to resell), and GSAP is now completely free, including SplitText, DrawSVG and MorphSVG. React Bits components are copy-paste, so we install only the ones we use and restyle them in navy and ultraviolet.

**Replacing the marquee**

- **Section names ride the racing line.** React Bits' Curved Loop / Text Loop flows text along a curved path. We feed it our racing line, so the section names travel along the circuit, and their speed follows how fast you scroll (Lenis gives us the scroll speed). GSAP DrawSVG draws the line itself as you scroll. This merges the marquee and the racing line into one signature effect.
- **Track change note:** when a section starts, the mini player flips to "Now playing: Experience" using **Split Flap Text** (the clacking flip letters of an F1 timing board or airport sign).
- Backup if the curve looks busy: React Bits' **Scroll Velocity** is the straight Dennis-style band, ready to drop in.

**Everywhere else**

- **Loader:** Split Flap Text for the "Warming up the tyres · 82%" line, and **Count Up** for the percentage.
- **Headings:** **Split Text** / **Masked Heading** (GSAP SplitText underneath) for the line-by-line reveal.
- **Intro chips:** **Rotating Text** cycles "Into F1 / football / EDM" before the chips appear.
- **Glass nav and mini player:** **liquidGL** makes them real refracting glass, like Apple's Liquid Glass. It's built to sync with Lenis and falls back to a normal blur on older browsers. We use it only on these two small elements, because it gets unstable in Safari on big areas.
- **Key buttons:** React Bits' **Magnet** on Drop in?, Resume and Email me only. **Specular Button** (a light glint that follows the cursor) is an option for Drop in?.
- **Project and role cards:** **Spotlight Card** or **Border Glow** for the booth-light sweep.
- **Certifications:** React Bits' **Lanyard** is a 3D badge hanging on a physics lanyard that you can grab and swing. It's exactly our backstage-pass idea. Desktop only, built on React Three Fiber, with flat cards on phones.
- **Custom cursor:** **Target Cursor**, **Glow Cursor** and **Blob Cursor** go into the cursor exploration, so you can try each one live.
- **Stats:** Count Up for 278 scenarios, 214,993 laps, and so on.
- **Skills:** **Logo Loop** for a slow strip of tool logos inside the mixer channels.
- **Tracklist filters:** **Animated List** for the re-sort animation.
- **Booth mode atmosphere:** one subtle WebGL background (**Side Rays** or **Light Rays**) as the soft coloured light at the screen edges. Dark mode only, laptops only.
- **404 page:** **Fuzzy Text** or **Letter Glitch** for "Track not found".
- **Contact:** **Click Spark** when the email is copied.
- **React Three Fiber:** used for The Drop's particle morph and the Lanyard, and nothing else. Both load only when needed and never on phones.
- **Lenis + GSAP ScrollTrigger:** the backbone, already in the plan. They are officially documented to work together.

**Not using**

- **Vanta.** It is built on an old version of three.js and adds about 120 KB. Its own site says to use no more than one or two effects per page and that some don't work on phones. React Bits' backgrounds do the same job in modern React.
- **liquid-glass-react.** Its displacement effect doesn't show in Safari or Firefox, so a third of visitors would see a plain box. liquidGL covers all four major browsers.

**Performance rule:** at most one WebGL effect on screen at a time, everything heavy loads lazily, and phones get the light versions.

## Always-on UI

These pieces float above the page on every section. Following the Apple skill, they sit on translucent "glass" layers that content scrolls under, not solid bars.

| Piece | Where | What it does |
| --- | --- | --- |
| **Nav bar** | Top, glass | Your name (home), then Experience, Projects, Certifications, Leadership and Contact in page order, with Resume as a filled button at the end. The section you're in is underlined. On phones the links fold into a menu button. It shrinks slightly after the opening and never hides. |
| **Booth Lights switch** | In the nav, right | A small fader-style switch. Flips between daylight and booth mode (see below). |
| **Waveform scroll bar** | Right edge (desktop) | A thin vertical waveform that fills as you scroll, with section markers like cue points. Clicking a marker jumps to that section. On phones it becomes a thin progress line under the nav. |
| **Mini player** | Bottom-left | Shows the current "track" (the section name). It plays ambient music, **on by default**, with a mute button that's always visible and remembers the visitor's choice. |
| **Energy meter** | Inside the mini player | A slim mixer-style meter (green, amber, red) that rises as people explore. |
| **Achievements counter** | Inside the mini player | "3 / 8". Clicking it opens a small panel listing found and locked achievements, with hints for locked ones. |
| **Achievement popup** | Bottom-right | Slides in when something is unlocked (title, short line, soft sound if sound is on), stays about 4 seconds, then slides back out the way it came. |
| **Command palette** | Ctrl+K or ⌘K | A search box to jump to any section, project, the resume, or contact. On phones it's reached from the menu. |
| **Custom cursor** | Desktop only | A small ring that grows and labels itself on hover ("View", "Play", "Drag"). It's hidden on touch devices and when reduced motion is on, where the normal cursor returns. |

## Booth Lights: daylight vs booth mode

One site, two moods. The layout and content never change; only light, colour and atmosphere do.

|  | Daylight (light) | Booth (dark) |
| --- | --- | --- |
| Look | Direction B, Daylight Studio: off-white, midnight navy text, one ultraviolet accent | Direction A, Afterhours: near-black, soft white text, deck colours used sparingly |
| Booth render | The booth in a bright studio, like a product shot | The booth in the dark, screens and LEDs glowing |
| Extras | Clean, calm, nothing ambient | Soft coloured light at the screen edges, glows on hover, ambient music available |
| Default | Follows the visitor's system setting (light or dark), then remembers their choice |  |

**The switch moment (aesthetic, not gimmicky).** Flipping the switch dims the page like house lights over about 0.6 seconds: colours ease across, never a hard flash. The booth renders cross-fade between their lit and dark versions. If sound is on, a single soft low thump plays. Following the Apple skill, the brightness change is eased so it never jolts the eyes, and with reduced motion it's a plain quick cross-fade.

We tune this together once v1 is running. If it feels gimmicky, we make it quieter.

## Gamification v1

Everything you approved is feasible for the first version, so it's all in. The one thing that needs an extra step is a **shared** leaderboard, because it needs a small free database. Until that exists, best scores are saved in each visitor's own browser.

### Achievements (8 to start)

| # | Achievement | How it's found |
| --- | --- | --- |
| 1 | Doors open | Watch the start lights all the way through |
| 2 | Lights down | Flip the Booth Lights switch for the first time |
| 3 | Crate digger | Open three project case studies |
| 4 | Pit lane | Finish a pit stop |
| 5 | Sub-2.5 | Finish a pit stop under the target time |
| 6 | Top bins | Score a penalty |
| 7 | Power user | Open the command palette |
| 8 | Full set | Reach the end of the track (the Encore) |

Rules: each fires the popup once, progress is remembered in the visitor's browser, and the counter panel shows a hint for each locked one. Finding all 8 triggers the **drop** as a demo; you'll judge it, and if it's out we swap in a calmer reward (a backstage-pass card, a behind-the-scenes page, or an F1-livery theme).

### Energy meter

- Rises when visitors scroll into a new section, open a project, watch a video, play a game or find an achievement.
- Falls slowly after about 20 seconds idle, like a crowd cooling off.
- At 100% the drop fires (demo, same review as above), then the meter rests at a calm "peak".

### Pit stop (top-down first)

- A top-down pit box: the car slides in, and you press each wheel (or keys 1 to 4) in the order the lights show. A green light releases the car, and your time shows to the millisecond.
- It has sound (wheel guns, engine), screen shake on a mistake, and instant restart.
- If the top-down version doesn't land for you, I build the stylised 3D pit box as a comparison demo.

### Penalty shootout

- Drag or swipe to aim, release to shoot. The keeper dives with a reaction delay, so it's beatable but not trivial.
- Five shots per round, with a crowd sound and a scoreboard.

### Command palette

- Ctrl+K or ⌘K opens a search box with everything on the site (sections, projects, resume, email copy). You'll test it and decide if it stays.

## Motion and interaction rules

The Apple design skill you shared is the rulebook here. These are the rules from it that matter most for this site, translated into plain terms.

**1. React instantly.** Buttons respond the moment they're pressed (a tiny 3% shrink in 0.1 seconds), not when released. Nothing on the site makes people wait for an animation to finish before they can act.

**2. Everything can be interrupted.** If someone scrolls back mid-animation or closes a game while it's opening, the motion reverses smoothly from wherever it is, with no jump. That's why touchable things use springs (motion with physical weight) instead of fixed-length animations.

**3. Springs, with sensible defaults.**

| Use | Feel | Values |
| --- | --- | --- |
| Most UI (panels, cards, popups) | Settles smoothly, no bounce | damping 1.0, response 0.3 to 0.4 s |
| Things that are flicked or thrown (the penalty ball, a dragged card) | Slight bounce | damping about 0.8, response 0.3 to 0.4 s |
| Press feedback | Instant | 0.1 s |
| Reduced-motion fades | Gentle | 0.2 s cross-fade |

**4. Things leave the way they came.** The achievement popup slides in from the bottom-right and leaves to the bottom-right. Project pages grow out of the row you clicked and shrink back into it.

**5. Scroll animations follow the scroll.** The booth zoom and the reveal effects are tied directly to scroll position, so they never play "on their own" and fight the visitor (the Lando and Dennis feel).

**6. Glass, not walls.** The nav and mini player are translucent with a soft blur; content scrolls underneath. A soft fade replaces hard divider lines.

**7. Sound and motion land together.** When there is sound (games, achievements, the Booth Lights thump), it fires on the same frame as the visual. Sound is used only for meaningful moments. It's on by default and starts the moment the visitor first clicks, taps or presses a key, because browsers block sound before that. A mute button is always in view, and the site remembers the choice.

**8. Typography tightens as it grows.** Big headlines get tighter letter-spacing (about −2%), body text stays normal, and line height is tight on headlines and relaxed on body text.

**9. Reduced motion is a real version, not a broken one.** Slides and zooms become quick fades, the particle morph becomes a fade-in, the custom cursor turns off, and the loader is static. Nothing is lost, just calmer.

**10. Smoothness is the bar.** Only transform and opacity are animated (the cheap properties for the browser). Every effect gets checked in slow motion before shipping.

## Visual system (starting draft)

These are starting values so the first build looks intentional. You said you'll decide better once you see colours in the real UI, so v1 will have a small hidden "theme tuner" during development that lets us swap palettes live.

**Colour tokens**

| Token | Booth (A, dark) | Daylight (B, light) | Used for |
| --- | --- | --- | --- |
| Background | #0A0A0B | #F5F5F2 | Page |
| Surface | #141416 | #FFFFFF | Cards, panels |
| Text | #F5F5F7 | #1B2333 (midnight navy) | Headlines, body |
| Muted text | #A1A1A6 | #6E6E73 | Captions, meta |
| Line | #26262B | #E3E3DF | Dividers, outlines |
| Accent | #9B8CFF (ultraviolet) | #5B3DF5 (ultraviolet) | Buttons, links, the one highlight per screen |
| Deck colours | Pink #FF3D8B, orange #FF8A1F, green #33D17A | Same, used even more sparingly | Waveforms, CUE/PLAY, meters only |

Rule: one accent per screen, and deck colours only where the real hardware would show them.

**Type**

- Headlines: a tight grotesk (Inter Tight to start), large, letter-spacing about −2%, line height about 1.05.
- Body: Inter (or the system font, per the Apple skill), 17 to 18 px, line height 1.5.
- Numbers and data: JetBrains Mono, for BPM-style stats, timers and track numbers.
- Sizes scale with the screen and respect the visitor's text-size settings.

**Layout**

- A 12-column grid, content max width about 1280 px, 24 px gutters on desktop and 16 px on phones.
- Spacing in steps of 8. Corner radius: 12 for cards, 20 for large panels, fully round for pills.
- Generous whitespace: one idea per screen, Apple-style.

## Performance, accessibility and SEO targets

These are the numbers we hold the build to. They're targets to test against, not guarantees.

**Performance (you said it's very important)**

| Target | Value |
| --- | --- |
| Main content visible (LCP) on a mid-range phone over 4G | under 2.5 s |
| Layout jumping (CLS) | under 0.1 |
| Response to taps and clicks (INP) | under 200 ms |
| Lighthouse performance score | 90+ on mobile |
| Booth zoom frames | Loaded after the first screen is visible, lowest-resolution first, as compressed WebP/AVIF. Phones never download them |
| 3D and games | Loaded only when a visitor reaches or opens them |

How: name, role and buttons render as plain HTML instantly; the heavy show loads behind them.

**Accessibility**

- Everything works with a keyboard, with a visible focus ring; the games have keyboard controls and can be skipped.
- Text contrast meets WCAG AA in both modes.
- Reduced-motion and reduced-transparency versions, as in the motion rules.
- Videos are muted by default, with captions where there's speech.
- The drop and any flashes stay under 3 flashes per second (the photosensitivity limit).

**SEO**

- All text is real HTML rendered on the server, not baked into images or canvas.
- Each project gets its own page and URL, so case studies can be linked from your resume.
- A title, description and share image for every page (the booth render makes a great share card), plus Person structured data and a sitemap.

## Components and tools per section

You asked to reuse ready-made pieces where possible. This maps each part to a starting point; we check each one's licence and phone performance before using it.

| Part | Built with | Ready-made starting points |
| --- | --- | --- |
| Site framework | Next.js (React), Tailwind CSS | shadcn/ui for basics (buttons, dialogs, command palette) |
| Smooth scroll, scroll-tied animation | Lenis + GSAP ScrollTrigger | Osmo scroll and text-reveal recipes |
| Springs and interruptible motion | Motion (formerly Framer Motion) | Spring presets from the motion rules |
| Booth zoom | Frames exported from the Blender script, drawn to a canvas in step with the scroll | Apple-style image-sequence pattern |
| The Drop particle morph | Three.js via React Three Fiber | React Bits / Aceternity particle components as a base |
| Text reveals, hover effects, cursor | Motion + GSAP | React Bits text animations, Magic UI, Cuberto-style cursor |
| Tracklist expand-on-hover | Motion layout animations | Aceternity expandable cards as a base |
| Command palette | cmdk (used by shadcn/ui) | shadcn Command component |
| Achievement popup | Sonner toasts, restyled | shadcn Sonner |
| Pit stop and penalty games | Canvas 2D with a small physics helper | Written for us; small and self-contained |
| Sound | Howler.js, free CC0 sounds | Freesound, Pixabay audio |
| Shared leaderboard (later) | Supabase free tier | Needs a free account, created when we get there |
| Hosting | Vercel free tier | Your GitHub repo connects in one click |

## Project content plan

Built from your seven context files (SARAH, ZEN AI, TerraLens, Voice Agent QA, PITWALL, CivicFix, NABHA), plus your corrections of 7 Nov: PITWALL uses your updated resume numbers, CivicFix is solo, and NABHA keeps its end-to-end encrypted consultations. The wording rules are binding on the site.

| Project | Where it goes | Status shown | Headline on the card | Best visual |
| --- | --- | --- | --- | --- |
| **SARAH** (evidence-verified voice interviewer) | **The Drop** (featured) + Released #1 | Working prototype, evaluated | Can't score anything the candidate didn't actually say. 97.3% gap detection, 56/56 verified scores, κ = 0.731 | Screen recording of a voice call, the pipeline diagram, the per-persona score chart |
| **Voice Agent Testing Framework** (AutoMinds internship) | Released #2, and the top line of the Experience strip | Completed, still in use at AutoMinds | I built an AI that calls an AI to find its bugs before launch. 278 scenarios, 200+ graded calls, \~90 bugs surfaced, \~90% fixed | Architecture diagram, a mock PASS/FAIL verdict card, stats strip (278 · 11 · 7 · 3 · 200+ · \~90) |
| **PITWALL** (F1 race strategy optimizer) | Released #3, linked both ways with the pit-stop game | Live (Vercel + Render) | Race strategy decided by a model trained on 214,993 real laps across 32 circuits. R² 0.845, 2.63 s MAE on race weekends it never saw, and 200 Monte Carlo trials per strategy | Live demo link, the Silverstone safety-car insight (0 → 5.4 → 8.9 → 0 s), tyre-compound colours |
| **CivicFix** (civic issue reporting) | Released #4 | Completed (Design Thinking course project) | Report it. Track it. Fix it. Citizens report Delhi civic issues and follow them to Resolved | Report wizard map step, issue status timeline, admin City Health Score |
| **NABHA Telemedicine** (Team Console, SIH 2025, end-to-end encrypted consultations) | Released #5 | Prototype | Top 100 of 500+ teams at Bennett's Smart India Hackathon round. 10+ services, 3 languages | Your demo video, the architecture diagram, EN/HI/PA language switch |
| **ZEN AI** (campus front door) | **Unreleased IDs** | Building now | Routes 87% of real student questions to the right office (n = 53), vs 70% for keyword matching | Routing demo UI clip, survey stats |
| **TerraLens** (Hindi/Bengali climate stance) | **Unreleased IDs** | In progress, due 20 Nov 2026 | No numbers. Built: multilingual preprocessing, loaders, evaluation framework | Script-detection example (Devanagari / Bengali / romanised) |

**Wording rules the site must follow (from your files)**

- **SARAH:** say voice runs in the browser/console via LiveKit, and that telephony is planned. Show latency honestly: 3.0 s median end to end, with the breakdown, and say the target wasn't met. κ = 0.731 is quadratic-weighted, against one human rater, on 28 simulated turns. Use real diagrams and charts, not AI-generated images.
- **ZEN AI:** "started for Microsoft Innovate 2026, made it to Round 3", never finalist or winner. "Real student questions" only for the 87% (n = 53). Always show n on small samples. Dashboards, email handoff, Azure and router v2 are labelled planned or in progress. Don't claim the kNN check adds accuracy. No teammates mentioned.
- **TerraLens:** no accuracy or F1 numbers, don't say the dataset exists yet, and don't present TF-IDF as the approach. Solo project. It moves to Released with real numbers after 20 Nov.
- **Voice Agent QA:** you built the *testing* framework, never "built AutoMinds' receptionist". It's proprietary: no code, phone numbers, patient data, internal names or real screens, and no repo link. Mock visuals (like the verdict card) are fine. It lives only in the Experience section, never in the Tracklist.
- **PITWALL:** your project, with a credit line thanking Arnav Singh for his help (for example "with help from Arnav Singh"). Numbers match your updated resume: 214,993 laps, 32 circuits, 5-fold GroupKFold by race weekend, R² 0.845, 2.63 s MAE, 200 Monte Carlo trials per candidate strategy, FastAPI + Next.js/TypeScript, Feb to Jun 2026. Show the honest limits (Suzuka \~10 s, no wet races, no traffic modelled).
- **CivicFix:** solo, no other contributors credited. The live app's "AI" is a rule-based simulator behind an LLM-ready interface, so say "AI-assisted" or "LLM-ready", not "powered by Claude". The Express/Prisma backend is "designed and implemented", not "fully integrated". Never publish the demo account passwords.
- **NABHA:** your role is "Team lead and Full-Stack AI Engineer" in a team of six (the SIH requirement), and you developed the project. Present it as a prototype: the hospital and emergency data are sample data, and the skin-disease CNN (\~70% on 500 images) is a screening aid, not a diagnosis tool. Badge text: "Top 100 / 500+ teams · Smart India Hackathon 2025 · Bennett University".

**The "Unreleased IDs" card design:** a status badge, a "Built so far" list, a "Next" list and a GitHub link, so an in-progress project reads as momentum rather than as unfinished.

**Still needed:** a CivicFix live demo link and screenshots if you have them, and a SARAH voice-call recording, which is still the best asset on the whole site.

## Build order for Phase 4, and what I need from you

The riskiest, most visible pieces get proven first, so if something disappoints we find out early.

1. **Skeleton:** the Next.js site with all sections as plain, fast, accessible content, the nav, both themes and the theme tuner. This is already a usable portfolio on its own.
2. **Booth zoom:** export the frame sequence from your refined booth script and wire it to scroll. You review it here: does the opening wow you?
3. **Motion layer:** smooth scroll, text reveals, hover states, cursor, page transitions (the Lando/Dennis feel).
4. **Booth Lights switch**, tuned together.
5. **Tracklist and case-study pages** with real project content.
6. **Always-on UI:** waveform scroll bar, mini player, energy meter, achievements and popups, command palette.
7. **Games:** pit stop (top-down), then penalties. You playtest.
8. **The Drop** particle moment.
9. **Polish pass:** performance, accessibility, SEO checks, slow-motion motion review, phone testing.
10. **Launch** on Vercel.

**What I need from you**

- **Project details** for each project: what it is, your role, the stack, two or three numbers, links, and any screenshots or screen recordings. You said these are coming next.
- **A GitHub repository** for the site. Create an empty one on GitHub and tell me its name, and I'll connect it.
- **Your resume PDF** (the current one is fine to start) and the links for LinkedIn, GitHub and email.
- **A photo** of yourself, if you want one in the Intro. Optional.
- **Your refined booth script** whenever it's ready. Until then I'll use v3.
- **Review comments** on this plan. Anything you disagree with, comment on it here.
