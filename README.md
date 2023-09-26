# lab-ghpages

Github Pages lab repo.

NOTE: do not use me. =]

feature1

## Docs versioning

- install mike

- create v0.1.x

```bash
mike deploy --push v0.1.x
mike set-default v0.1.x
```

- create v0.2.x

```bash
echo 'version v0.2.x' > docs/index.md &&\
git add docs/index.md &&\
git commit -m 'version v0.2.x' docs/index.md
mike deploy --push v0.2.x latest
mike set-default v0.2.x
```

- create v0.3.x

```bash
VERSION=v0.3.x
echo "version $VERSION" > docs/index.md &&\
git add docs/index.md &&\
git commit -m "version $VERSION" docs/index.md
mike deploy --push $VERSION preview
```

- create v0.4.x

```bash
VERSION=v0.4.x
echo "version $VERSION" > docs/index.md &&\
git add docs/index.md &&\
git commit -m "version $VERSION" docs/index.md
#mike deploy --push $VERSION preview
```

- create v0.5.x

```bash
VERSION=v0.5.x
echo "version $VERSION" > docs/index.md &&\
git add docs/index.md &&\
git commit -m "version $VERSION" docs/index.md
mike deploy --push $VERSION preview
```

- create warning

- testing

```bash
mike serve -a 0.0.0.0:8181
```