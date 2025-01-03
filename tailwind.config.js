/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html",
    "./static/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        outfit: ["Outfit", "sans-serif"],
      },
      colors: {
        gradientStart: '#130428',
        gradientMid1: '#251043',
        gradientMid2: '#381E6D',
        gradientMid3: '#261045',
        gradientEnd: '#190634',
      },
      backgroundImage: {
        'custom-gradient': 'linear-gradient(150deg, #130428 14%, #251043 34%, #532d9b 80%, #623b9b 85%, #a36eed 100%)',
        'background':'linear-gradient(180deg, #001831 14%, #001831 34%, #001831 80%, #18003e 85%, #19a7e5 100%)'
      }

    },
  },
  plugins: [],
}

