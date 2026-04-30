# mkdocs
ocf mkdocs real?

## Development
1. clone the repo
1. `nix develop`
    - ensure flakes and nix-command features are enabled
1. `mkdocs serve`
1. `rm -rf docs/'Board of Directors Minutes'` so it builds faster lol

### Why isn't Board of Directors visible in development?

We have a lot of BoD notes, which makes mkdocs rebuild very slowly (20-30 seconds). The shell hook for `nix develop` runs `mkdocs serve -f mkdocs-dev.yml` which ignores the `bod` directory. Run `mkdocs serve -f mkdocs-dev` if you need to see BoD notes on localhost.

## TODO

- fix constitution links
- fix mobile navigation menus turning white on dark theme
- make private docs more accessible

- migrate https://decal.ocf.io/resources to startertasks.md and remove from decal-web
- BoD notetaking procedure
- fix officers.md
- fix relative links
- add hosting badges images

- look into setting the page status (deprecated in particular)
- hide toc/navigation on pages with little content
- search boost important pages
- add announcements
- add socials in footer
- social card branding (ask jingwen)
