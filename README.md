# shaurya-portfolio

Personal portfolio of **Shaurya Nigam**, Full-Stack AI Engineer. A DJ-booth themed, scroll-driven site.

## Stack

Next.js (App Router) · TypeScript · Tailwind CSS · shadcn/ui · Lenis + GSAP + Motion · React Three Fiber (lazy, two effects only) · Howler

## Run it locally

```bash
npm install
npm run dev
```

Then open http://localhost:3000.

## Layout

| Path | What's there |
| --- | --- |
| `docs/` | Private planning notes (local only, not in this repo) |
| `src/app` | Pages, layout and the global theme (`globals.css`) |
| `src/components/sections` | One component per page section |
| `src/components/ui` | Shared UI pieces |
| `src/components/games` | Pit stop and Penalty shootout |
| `src/lib` | Helpers (scroll setup, sound manager) |
| `public/booth`, `public/audio` | Rendered booth frames and sounds |
| `booth-blender` | Blender scripts that render the booth |
