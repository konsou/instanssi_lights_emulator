# Instanssi Lights Emulator

The Instanssi Lights Emulator is a Python-based application designed to simulate the lighting setup typically found at the Instanssi demo party. It listens for UDP packets on a configurable port and updates the virtual lights' states based on the received data, displaying these states as colored circles on a graphical interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python 3.8 or newer installed on your system. This project does not support older versions of Python.

### Setting Up the Project

1. **Clone the repository**:

```bash
git clone https://github.com/konsou/instanssi_lights_emulator.git
cd instanssi_lights_emulator
```

2. **Create a virtual environment** in the `.venv` folder:

```bash
python -m venv .venv
```

3. **Activate the virtual environment**:

- On Windows:

```bash
.venv\Scripts\activate
```

- On Unix or MacOS:

```bash
source .venv/bin/activate
```

4. **Install the required packages** using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Running the Emulator

To start the emulator, run the `main.py` script from the command line:

```bash
python main.py
```

### Sending Test Data

To send test data to the emulator, you can use the `test.py` script. This script simulates data packets that control the lights:

```bash
python test.py
```

Ensure the emulator is running before you send test data.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- Inspiration from the Instanssi demo party organizers.
- The [Valoserveri project](https://github.com/turol/valoserveri), the lights server used at Instanssi.
- Visit [Instanssi's main website](https://instanssi.org/) to learn more about the demo party.
