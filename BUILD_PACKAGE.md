1. Build package
```bash
python -m build
```

2. Update to Test PyPi
```bash
twine upload --repository testpypi dist/*
```