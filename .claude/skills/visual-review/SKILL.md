---
name: visual-review
description: Look at the site in a real browser after any change to its look, layout or animation, find problems, fix them and check again. Use after every UI change, before telling the user it is done.
---

# Visual review

Open the site in a real browser with `playwright-cli`, look at what was built, fix what is wrong, and check again. The user watches in a headed window. For the commands, see the `playwright-cli` skill.

## Before you start

- Read `docs/plan.md` (private, never commit it) and the `apple-design` skill. Review against both.
- Never put the phone number anywhere, including notes, summaries and comments.
- Note which section(s) changed. You will screenshot those plus the full page.

## 1. Start the site

1. If `http://localhost:3000` already responds, reuse that dev server. Otherwise run `npm run dev` in the background and wait until it responds.
2. Open it headed so the user can watch: `playwright-cli open http://localhost:3000 --headed`.

## 2. Take screenshots

Save into `review/` (git-ignored). Use names like `round1-before-laptop-light-intro.png`. Take both:

- the **changed section** (element screenshot, or scroll to it)
- the **full page** (`--full-page`)

For each combination:

| Size | Command |
| --- | --- |
| Laptop 1440×900 | `playwright-cli resize 1440 900` |
| Phone 390×844 | `playwright-cli resize 390 844` |

| Mode | Command |
| --- | --- |
| Light | `playwright-cli set-color-scheme light` |
| Dark | `playwright-cli set-color-scheme dark` |

That is 2 sizes × 2 modes × (section + full page) = 8 shots per round. Reload after changing size or colour scheme if the layout depends on it. Remember phones skip the booth, so go straight from Loader to Intro at 390 wide. Take "before" shots in round 1, before any fix, and keep them.

If `prefers-reduced-motion` was touched, also check the calm static alternative.

## 3. Check for errors

- `playwright-cli console` (errors and warnings) and `playwright-cli requests`.
- Report any console errors, failed or 404 loads, and anything heavy loading too early (three.js, games, booth frames, audio must be lazy; phones must never request booth frames or clips).

## 4. Click through what changed

Interact with every piece that changed:

- buttons, nav links and hover states
- keyboard: arrow keys and `1`–`4` on the booth, `Esc`, `Ctrl+K`
- scroll through the whole page, top to bottom, watching for jumps and jank

## 5. Review

Look at each screenshot (Read the image files) against `docs/plan.md` and the `apple-design` skill. Look for:

- spacing and alignment
- text that overflows or is cut off
- contrast, in both light and dark
- colours: navy text, ultraviolet accent
- anything broken on the phone size
- anything cluttered or not "Apple-clean"

## 6. List, fix, re-check

1. Write a short list of problems, **most serious first**.
2. Fix them, then repeat from step 2 (the new shots are the "after").
3. **At most 3 rounds.** Stop earlier if nothing is left to fix.

## 7. Wrap up

Close the browser (`playwright-cli close`). Show the user a short summary:

- what you found and fixed, per round
- what is still open
- paths to the before and after screenshots in `review/`
- any suggestions that need the user's decision

## Hard rule

**Never change the plan's decisions on your own**: colours, sections, wording rules, or anything else `docs/plan.md` settles. If a review suggests changing one, do not do it. Put it in the summary as a suggestion for the user.
