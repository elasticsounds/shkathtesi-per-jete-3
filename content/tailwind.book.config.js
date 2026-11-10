/** Book-only Tailwind configuration. The reader's global reset is intentionally disabled. */
module.exports = {
  content: ["../../*.html", "../navigation/*.html"],
  corePlugins: { preflight: false },
  theme: {
    extend: {
      colors: {
        "spj-purple": "#76539d",
        "spj-sky": "#087eb8",
        "spj-teal": "#138e9c",
        "spj-amber": "#f4a300",
        "spj-coral": "#df4f62",
        "spj-lime": "#6e9f00",
        "spj-ink": "#172033",
        "spj-paper": "#fffdf7",
      },
      fontFamily: {
        book: ["Atkinson Hyperlegible", "Merriweather", "sans-serif"],
        display: ["Merriweather", "Atkinson Hyperlegible", "serif"],
      },
    },
  },
};
