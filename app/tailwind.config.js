/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors: {
        text_blue: "#1d4ed8",
        active_blue: "#dbeafe",
        hover_blue: "#2563eb",
        focus_blue: "#2563eb",
      },
      fontSize: {
        ph_size: "16px",
        btn_size: "16px",
      },
    },
  },
  plugins: [],
};
