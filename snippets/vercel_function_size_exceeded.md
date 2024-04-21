# ERROR: A Serverless Function has exceed the unzipped maximum size of 250 MB. : https://vercel.link/serverless-function-size

## Situation

- Vercel NextJS 14 + Python project
- Python serverless function bundle size exceeded 250 MB

## Vercel Serverless Functions Size Exceeded Error

When deploying a Vercel NextJS + Python project, you may encounter the following error:

```
Error: A Serverless Function has exceeded the unzipped maximum size of 250 MB. : https://vercel.link/serverless-function-size
```

This seems to be particularly common with using the python runtime for serverless functions, the root cause appears to 
be that a bunch of node modules, caches, and other files are being included in the Python serverless function bundle.

## Fix

### What DOESN'T WORK

For some reason, the [docs](https://vercel.com/docs/projects/project-configuration#functions) suggest that 
`vercel.json`'s `functions` shouldn't be supported in Next.js.

Instead, the [docs](https://nextjs.org/docs/app/api-reference/next-config-js/output#caveats) suggest using 
`next.config.js` like so:
```javascript
module.exports = {
  experimental: {
    outputFileTracingExcludes: {
      './api/index': ['./un-necessary-folder/**/*'],
    },
  },
}
```

However, this doesn't seem to work for Python serverless functions. I attempted the following but it seems to do next
to nothing:
```
/** @type {import("next").NextConfig} */

const nextConfig = {
    experimental: {
        outputFileTracingExcludes: {
            "*": ["./node_modules/**/@swc/core*"],
            "./api/*": [
                "./**/cache/**/*",
                "./**/.cache/**/*",
                "./src/**/*",
                "./prisma/**/*",
                "./**/*",
            ],
            "./api/index": [
                "./**/cache/**/*",
                "./**/.cache/**/*",
                "./src/**/*",
                "./prisma/**/*",
                "./**/*",
            ],
        },
    },
};

module.exports = nextConfig;
```

Only that first line `"*": ["./node_modules/**/@swc/core*"]` seems to do anything.

### What WORKS

Using `vercel.json` to exclude files from the python serverless functions seems to work:
```
{
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "/api/index"
    }
  ],
  "functions": {
    "api/index.py": {
      "excludeFiles": "{node_modules,src,*.cache,public,cache,app,.next}/**"
    }
  }
}
```
Here, `api/index.py` is a flask based serverless function, and the `excludeFiles` key is used to exclude the specified
files from the serverless function bundle.

## Debugging and Process Tips

- Running `vercel build --debug` locally to manually inspect the contents of the Python serverless function bundle
  - Note that you want to stash or commit any changes before running this, so that you can easily discard the changes
    after running the command. Use `git clean -df` is a good way to discard changes.
- Checking the logs on Vercel's dashboard for function execution errors
  - One mistake I ran into was a particular Python package not being supported in Python 3.9 (locally using 3.11), which
    caused the serverless function to fail on Vercel due to "package not found"/"package can't be imported" errors.

## References
- https://github.com/orgs/vercel/discussions/103#discussioncomment-6952635
- https://github.com/vercel/vercel/issues/2830#issuecomment-583177480
- https://github.com/orgs/vercel/discussions/4354
- https://github.com/orgs/vercel/discussions/103#discussioncomment-6356642
- https://nextjs.org/docs/app/api-reference/next-config-js/output
- https://vercel.com/docs/cli/build
- https://vercel.com/docs/projects/project-configuration
- 