# Mr Wolf

The Mr Wolf webapp for [cedwyn.bucklerfamily.estate/mr-wolf/](https://cedwyn.bucklerfamily.estate/mr-wolf/), maintained in its own repository.

## Source of truth

This repository is the canonical source (`split-repos.json` in `unclehowell/cedwyn` sets Mr Wolf to `split-repo`). The old `section/mr-wolf` branch in `unclehowell/cedwyn` is a compatibility mirror for the consolidated Cedwyn site. **Send changes as pull requests to this repository's `main` branch**, not to the old mirror.

After a PR is merged, Cedwyn's split-repository sync copies this repository's `main` back into `section/mr-wolf`; the consolidated site then consumes that snapshot through `sections.lock` and its normal site build. Do not force-push or delete the old branch.

## Pull request previews

The Cloudflare Pages account is at its project limit, so Mr Wolf cannot have a second, separately Git-connected Pages project at present. The existing `cedwyn` Pages project is Git-connected to the consolidated repository and has a dedicated `staging/*` preview allow-list.

For this review, the v2.1.0 full-site snapshot is staged on `unclehowell/cedwyn` branch `staging/mr-wolf-v2.1.0-preview`. Cloudflare serves that isolated branch at:

[Mr Wolf v2.1.0 staging preview](https://staging-mr-wolf-v2-1-0-previ.cedwyn-274.pages.dev/mr-wolf/)

The PR workflow comments this preview URL; it does not deploy or modify production. The staging snapshot is separate from this PR and must be refreshed when the PR content changes. The consolidated production branch remains `site`.

## Get the code

```sh
git clone --depth 1 https://github.com/unclehowell/cedwyn-mr-wolf.git
```

History before the split: https://github.com/unclehowell/cedwyn/commits/section/mr-wolf
