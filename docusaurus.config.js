// @ts-check

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Model Health Documentation',
  tagline: 'Guides, best practices and reference for using Model Health',
  favicon: 'img/favicon.ico',

  url: 'https://docs.modelhealth.io',
  baseUrl: '/',

  organizationName: 'model-health',
  projectName: 'model-health-docs',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  customFields: {
    DOCUSAURUS_API_URL: process.env.DOCUSAURUS_API_URL,
    BUILD_ENV: process.env.BUILD_ENV,
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          path: 'docs',
          routeBasePath: 'docs',
          sidebarPath: require.resolve('./docs-sidebars.js'),
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'light',
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'Model Health',
        logo: {
          alt: 'Model Health Logo',
          src: 'img/logo.png',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'productSidebar',
            position: 'left',
            label: 'Documentation',
          },
          {
            href: 'https://sdk.modelhealth.io',
            label: 'SDK',
            position: 'left',
          },
        ],
      },
      footer: {
        style: 'light',
        copyright: `Copyright © ${new Date().getFullYear()} Model Health.`,
      },
      prism: {
        theme: require('prism-react-renderer').themes.github,
        darkTheme: require('prism-react-renderer').themes.dracula,
        additionalLanguages: ['swift', 'typescript', 'bash', 'python'],
      },
    }),
};

module.exports = config;
