# Mr Wolf

The Mr Wolf webapp for [cedwyn.bucklerfamily.estate/mr-wolf/](https://cedwyn.bucklerfamily.estate/mr-wolf/), maintained in its own repository.

## Source of truth

This repository is the canonical source (`split-repos.json` in `unclehowell/cedwyn` sets Mr Wolf to `split-repo`). The old `section/mr-wolf` branch in `unclehowell/cedwyn` is a compatibility mirror for the consolidated Cedwyn site. **Send changes as pull requests to this repository's `main` branch**, not to the old mirror.

After a PR is merged, Cedwyn's split-repository sync copies this repository's `main` back into `section/mr-wolf`; the consolidated site then consumes that snapshot through `sections.lock` and its normal site build. Do not force-push or delete the old branch.

## Pull request preview

Every PR runs `.github/workflows/preview.yml`. It deploys an isolated preview to Cloudflare Pages project `cedwyn-mr-wolf` and comments a URL ending in `/mr-wolf/`. The preview does not update the production Cedwyn site. The workflow requires repository secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`.

## Get the code

```sh
git clone --depth 1 https://github.com/unclehowell/cedwyn-mr-wolf.git
```

History before the split: https://github.com/unclehowell/cedwyn/commits/section/mr-wolf
