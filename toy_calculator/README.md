# Toy Calculator

A simple Python calculator with basic arithmetic operations.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run the test suite:

```bash
pytest
```

## Code Coverage

Generate code coverage reports:

```bash
# Generate coverage report in terminal and HTML
pytest --cov=calculator --cov-report=html --cov-report=term

# Generate coverage report in XML format (for CI/CD)
pytest --cov=calculator --cov-report=xml
```

## Uploading Coverage to Datadog

To upload code coverage reports to Datadog, you'll need a valid Datadog API key. You can use `npx` to run the Datadog CI tool without installing it globally:

```bash
# Set your Datadog API key
export DD_API_KEY="your_api_key_here"

# Upload coverage reports (recursively searches current directory)
npx @datadog/datadog-ci coverage upload .

# Or specify specific coverage files
npx @datadog/datadog-ci coverage upload .coverage htmlcov/
```

### GitHub Actions Example

```yaml
steps:
- name: Upload coverage reports to Datadog
  run: npx @datadog/datadog-ci coverage upload .
  env:
    DD_API_KEY: ${{ secrets.DD_API_KEY }}
    DD_SITE: datadoghq.com
```

## Functions

- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract b from a
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide a by b (raises ValueError for division by zero) 