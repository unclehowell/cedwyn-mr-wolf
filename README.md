# Mr Wolf

The Mr Wolf webapp for [cedwyn.bucklerfamily.estate/mr-wolf/](https://cedwyn.bucklerfamily.estate/mr-wolf/), maintained in its own repository.

## Source of truth

This repository is the canonical source (`split-repos.json` in `unclehowell/cedwyn` sets Mr Wolf to `split-repo`). The old `section/mr-wolf` branch in `unclehowell/cedwyn` is a compatibility mirror for the consolidated Cedwyn site. **Send changes as pull requests to this repository's `main` branch**, not to the old mirror.

After a PR is merged, Cedwyn's split-repository sync copies this repository's `main` back into `section/mr-wolf`; the consolidated site then consumes that snapshot through `sections.lock` and its normal site build. Do not force-push or delete the old branch.

## Pull request previews

Cloudflare Pages project `cedwyn-mr-wolf` is connected directly to this repository. It uses `main` as its production branch, deploys preview branches, and posts the primary preview URL automatically on each pull request. The stable branch preview for this review is:

[Mr Wolf v2.1.0 app preview](https://legal-threshold-v2-1-0-previ.cedwyn-mr-wolf.pages.dev)

A second, supplementary preview shows the app inside the full consolidated Cedwyn site. The PR workflow posts that link from the `staging/mr-wolf-v2.1.0-preview` snapshot in `unclehowell/cedwyn`. That snapshot is separate from the split-app PR and must be refreshed after PR content changes.

Neither preview changes the consolidated production `site` branch or custom domains. Merging this PR updates the standalone Pages project's `main` deployment; Cedwyn's separate sync and consolidated site build remain the release path for the primary family site.

## Get the code

```sh
git clone --depth 1 https://github.com/unclehowell/cedwyn-mr-wolf.git
```

History before the split: https://github.com/unclehowell/cedwyn/commits/section/mr-wolf
