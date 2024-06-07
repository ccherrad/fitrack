// @ts-check
import withNuxt from "./.nuxt/eslint.config.mjs";

// Your custom configs here
export default withNuxt({
  rules: {
    "comma-dangle": ["error", "always-multiline"],
    "semi": ["error"],
    "no-trailing-spaces": ["error"],
    "no-extra-semi": ["error"],
    "quotes": ["error", "double"],
    "@typescript-eslint/member-delimiter-style": [
      "error", {
        "multiline": {
          "delimiter": "semi",
          "requireLast": true,
        },
        "singleline": {
          "delimiter": "semi",
          "requireLast": false,
        },
      },
  ],
  },
});