# mkdocs
ocf mkdocs real?

## how to add docs page
1. create markdown file
2. dont forget to add to nav structure in mkdocs.yml! this is necessary to declare the order docs show up in. otherwise, your doc will be hidden from the public table of contents.
    1. yes moving things around sucks. just use good vim substitution commands! :)

## Development
1. clone the repo
1. `nix develop`
1. `mkdocs serve`
1. `rm -rf docs/'Board of Directors Minutes'` so it builds faster lol

## TODO
- remove meta titles
- add socials in footer
- fix officers.md
- fix relative links
- add hosting badges page!
- decide on dark color palette

- look into setting the page status (deprecated in particular)
- hide toc/navigation on pages with little content
- search boost important pages
- social card branding (ask jingwen)
- add announcements
