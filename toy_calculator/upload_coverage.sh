#!/bin/bash

# Script to upload code coverage reports to Datadog
# Make sure to set your DD_API_KEY environment variable first

echo "🚀 Uploading code coverage reports to Datadog..."

# Check if API key is set
if [ -z "$DD_API_KEY" ]; then
    echo "❌ Error: DD_API_KEY environment variable is not set"
    echo "Please set it with: export DD_API_KEY='your_api_key_here'"
    echo ""
    echo "You can get your API key from: https://app.datadoghq.com/account/settings#api"
    exit 1
fi

# Check if coverage files exist
if [ ! -f "coverage.xml" ]; then
    echo "❌ Error: coverage.xml not found"
    echo "Please run: pytest --cov=calculator --cov-report=xml"
    exit 1
fi

echo "✅ Found coverage.xml"
echo "✅ API key is set"
echo ""

# Upload coverage reports
echo "📤 Uploading coverage reports..."
npx @datadog/datadog-ci coverage upload .

if [ $? -eq 0 ]; then
    echo "✅ Coverage reports uploaded successfully!"
    echo "📊 Check your Datadog dashboard for coverage data"
else
    echo "❌ Failed to upload coverage reports"
    exit 1
fi 