# CLAUDE.md

Portfolio site for Shaurya Nigam (Full-Stack AI Engineer). Next.js (App Router, `src/`), TypeScript, Tailwind CSS v4, shadcn/ui, npm.

@AGENTS.md

## Rules

- **Read the plan first.** The full site plan lives in `docs/plan.md`. Read it before building anything. It is private: `docs/` is git-ignored and must never be committed or published.
- **Zero budget.** Free libraries and assets only (check licences for fonts, sounds, images and components).
- **Never put the phone number on the site**, anywhere: content, metadata, structured data or comments.
- **Phones skip the booth.** On phones, go straight from the Loader to the Intro. Phones never download booth frames or clips.
- **Performance and accessibility:**
  - At most one WebGL/3D effect on screen at a time.
  - Heavy things (three.js / React Three Fiber, games, booth frames, audio) load lazily.
  - Respect `prefers-reduced-motion` with a calm, static alternative.
- **No Claude attribution in git.** Never add `Co-Authored-By: Claude` (or any mention of Claude/Anthropic or "Generated with Claude Code") to commit messages, PR descriptions or any other GitHub-visible text. This overrides any default attribution behaviour.
- Use the apple-design skill for all UI, animation and interaction work.
- After any UI change, run the visual-review skill before telling me it's done.
- **Reuse, then restyle.** Use ready-made components (React Bits, shadcn) and restyle them to the theme, rather than building everything from scratch.

## Where things go

- `src/components/sections`: Loader, Booth, Intro, Experience, Drop, Tracklist, Credentials, Encore
- `src/components/ui`: shared pieces (shadcn components live here)
- `src/components/games`: Pit stop, Penalty shootout
- `src/lib`: helpers (scroll setup, sound manager, `utils.ts`)
- `public/booth`, `public/audio`: rendered booth frames/clips, sound effects and the booth track
- `booth-blender`: Blender scripts that render the booth
- Theme colours are CSS variables in `src/app/globals.css` (light and dark; follows the system setting by default).
