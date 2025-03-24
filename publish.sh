#!/bin/bash

echo "🔄 Cleaning previous builds..."
rm -rf build dist *.egg-info

echo "⬆️  Bumping patch version..."
bump2version patch || exit 1

echo "🚀 Pushing to GitHub..."
git push && git push --tags

echo "📦 Building package..."
python setup.py sdist bdist_wheel

echo "📤 Uploading to PyPI..."
twine upload dist/*

echo "✅ Done!"
