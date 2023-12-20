module.exports = {
  extends: ['airbnb', 'airbnb-typescript', 'next/core-web-vitals', 'eslint:recommended', 'plugin:@typescript-eslint/recommended'],
  root: true,
  overrides: [
    {
      files: ['*.d.ts', '*.ts', '*.tsx'],
      parser: '@typescript-eslint/parser',
      parserOptions: {
        project: './tsconfig.json',
        tsconfigRootDir: __dirname
      },
      plugins: ['@typescript-eslint'],
      rules: {
        'import/extensions': [
          'error',
          'ignorePackages',
          { // Fixes: Missing file extension for "@/some-file" eslint(import/extensions)
            '': 'never',
            js: 'never',
            jsx: 'never',
            ts: 'never',
            tsx: 'never',
          }
        ],
        'react/jsx-props-no-spreading': 0,
        '@typescript-eslint/explicit-function-return-type': 'error'
      }
    }
  ]
}