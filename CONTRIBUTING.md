# Contributing to AegisLab

Thank you for your interest in contributing to AegisLab! This project demonstrates cybersecurity detection and analysis capabilities in a safe, legal lab environment.

## Code of Conduct

This project adheres to our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## How to Contribute

### Reporting Issues
- Check existing issues before creating new ones
- Use clear, descriptive titles
- Include reproduction steps for bugs
- Label appropriately (bug, enhancement, question)

### Development Setup

1. **Clone and setup environment:**
   ```bash
   git clone https://github.com/dukeblue1994-glitch/aegislab.git
   cd aegislab
   pip install -r tools/requirements.txt
   ```

2. **Test the pipeline:**
   ```bash
   python tools/aegisctl.py synth
   python tools/aegisctl.py analyze
   python tools/aegisctl.py report
   ```

3. **Run tests:**
   ```bash
   pytest tests/ -v
   flake8 tools/ emulation/
   ```

### Pull Request Process

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-detection`
3. **Make** your changes with clear commits
4. **Add** tests for new functionality
5. **Ensure** CI pipeline passes
6. **Update** documentation as needed
7. **Submit** pull request with description

### Contribution Guidelines

#### Sigma Rules
- Follow [Sigma specification](https://github.com/SigmaHQ/sigma)
- Include clear descriptions and ATT&CK mappings
- Test rules with synthetic data
- Use appropriate log sources

#### Python Code
- Follow PEP 8 style guidelines
- Add docstrings for functions/classes
- Include unit tests for new features
- Keep functions focused and testable

#### Security Considerations
- All synthetic data must be clearly marked as fake
- No real exploit code or malicious payloads
- Maintain ethical use focus
- Document security implications

### Areas for Contribution

- 🔍 **Detection Rules**: New Sigma rules for different attack patterns
- 📊 **Analytics**: Enhanced analysis algorithms
- 🐳 **Infrastructure**: Docker improvements, monitoring
- 📚 **Documentation**: Tutorials, examples, architecture docs
- 🧪 **Testing**: Additional test cases, edge case handling
- 🎨 **Visualization**: Dashboards, reporting improvements

### Questions?

Feel free to open an issue for questions about:
- Architecture decisions
- Implementation approaches
- Best practices
- Feature requests

## License

By contributing, you agree that your contributions will be licensed under the MIT License.