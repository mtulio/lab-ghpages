# lab-ghpages

Github Pages lab repo.

NOTE: do not use me. =]

feature1

## Docs versioning

- install mike

- create v0.1.x

```bash
mike deploy --push v0.1.x
```

- create v0.2.x

```bash
mike deploy --push v0.2.x latest
mike set-default v0.2.x
```

- create v0.3.x

```bash
mike deploy --push v0.2.x preview
```

- create warning