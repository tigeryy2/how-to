# Frontend References

Javascript, Typescript, React, Next.JS references. For now, catch-all while I give myself a frontend
crash course..

## Environment Setup

Environment setup for frontend dev.

### node.js and npm

Use [nvm](https://github.com/nvm-sh/nvm), a node version manager, to install node.

Installs via [script](https://github.com/nvm-sh/nvm#install--update-script)

Verify with `command -v nvm`, which should output `nvm`. See [usage](https://github.com/nvm-sh/nvm#usage)

To install latest node: `nvm install node` or specific version: `nvm install 14.7.0`.

Switch between versions with `nvm use node`, to override the default in each new shell.

See [installing node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

### next.js and React

Use `npm install next@latest react@latest react-dom@latest` or `npx create-next-app@latest` for auto setup.

See [nextjs installation](https://nextjs.org/docs/getting-started/installation)

## Getting Started

Getting started...

### next.js boilerplate

See [vercel nextjs template](https://github.com/vercel/vercel/tree/main/examples/nextjs)

### Installing Prettier and Prettier Configuration

To add prettier to a project, run `npm install prettier --save-dev`

Configuration can be done via the `package.json` file, or a `.prettierrc` file.

For example, to configure prettier to use 4 spaces instead of 2, add the following to `package.json`:

```json
  "prettier": {
"tabWidth": 4
},
```

### Tailwind CSS

Install prettier plugin for tailwind, to automatically sort tailwind classes.

Run:

```bash
npm install -D prettier prettier-plugin-tailwindcss
```

### Storybook and NextJS integration

When integrating Storybook with NextJS, may need to manually add the following to `.storybook/main.js`:

```typescript
    import path from "path";
    const config: StorybookConfig = {
    // ... other config

    webpackFinal: async (config: any) => {
        config.resolve.alias["@"] = path.resolve(__dirname, "../src");
        config.resolve.alias["@/components"] = path.resolve(
            __dirname,
            "../src/components",
        );

        return config;
    },
    }
```

This should match the `tsconfig.json` paths, and allow Storybook to resolve the paths correctly.

See [github issue](https://github.com/storybookjs/storybook/issues/12449#issuecomment-1637153787)

### Vercel Serverless Functions

Note: Can't seem to use both Node and non-node serverless functions in the same project.
See https://github.com/vercel/vercel/discussions/6197.

Python serverless functions go in `/api` directory.
Node serverless functions go in `/pages/api` directory.
Can't seem to have both at the same time.

Further, to use Python serverless functions locally, need to use `vercel dev` instead of `npm run dev`.`

## Libraries and Tools

Useful libraries and tools.

### Authentication next-auth

See [github](https://github.com/nextauthjs/next-auth) and [website](https://next-auth.js.org/)

### Component Libraries

[shadcn/ui](https://ui.shadcn.com/docs) - Shadcn UI component library
[Prism UI](https://www.prismui.tech/) - Prism UI component library, builds on top of Shadcn UI