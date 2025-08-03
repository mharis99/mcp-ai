/** @type {import('@remix-run/dev').AppConfig} */
module.exports = {
  appDirectory: "app",
  serverBuildTarget: "vercel",
  server: "./server.js", // This tells Remix to use custom server (which will be Vercel’s runtime)
  ignoredRouteFiles: ["**/.*"]
};
