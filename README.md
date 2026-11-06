# Mr Wolf

The Mr Wolf webapp of [cedwyn.bucklerfamily.estate](https://cedwyn.bucklerfamily.estate/mr-wolf/), in its own repository
(webapp migration 59+1, issue #188 on unclehowell/cedwyn).

Split out of `unclehowell/cedwyn` branch `section/mr-wolf` on 5 Nov 2026. That repository holds about 300 branches; a job on one webapp
should never need the rest.

## Get the code

```
git clone --depth 1 https://github.com/unclehowell/cedwyn-mr-wolf.git
```

## Where to send changes

The current `split-repos.json` entry in `unclehowell/cedwyn` sets this app to `mode: split-repo`. **This repository's `main` branch is the source of truth.**

1. Make application changes on a feature branch in this repository.
2. Open a pull request into this repository's `main`.
3. After merge, Cedwyn's scheduled `sync-split-repos` workflow copies `main` into the retained legacy branch `section/mr-wolf`.
4. The central `build-cedwyn` workflow assembles the unified site from the synced branch.

Do not open application pull requests against the legacy branch `section/mr-wolf`; it is a compatibility mirror, not the development target. Site-wide registry, shared runtime, central catalogue and build changes still belong in `unclehowell/cedwyn` `main`.

Full instructions: [REPO-SPLIT.md](https://github.com/unclehowell/cedwyn/blob/main/docs/REPO-SPLIT.md).


## Preview

Cloudflare Pages project `cedwyn-mr-wolf` builds every branch and pull request: https://cedwyn-mr-wolf.pages.dev/

## History before the split

https://github.com/unclehowell/cedwyn/commits/section/mr-wolf

Never force-push; never delete the old branch.
