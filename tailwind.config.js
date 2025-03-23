/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html",
    "./static/*.js",
    "*"
  ],
  theme: {
    extend: {
      fontFamily: {
        outfit: ["Outfit", "sans-serif"],
      },
     
      backgroundImage: {
        'custom-gradient': 'linear-gradient(150deg, #130428 14%, #1d0343 34%, #004564 80%, #00506e 85%, #0384ad 100%);',
        'background':'linear-gradient(180deg, #001831 14%, #001831 34%, #001831 80%, #18003e 85%, #19a7e5 100%)'
      }

    },
  },
  plugins: [],
}

