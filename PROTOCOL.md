# Instanssi Lights Control Protocol Specification
Adapted from https://github.com/turol/valoserveri/blob/master/use_examples/over_udp.py. License information at the bottom of this file.

## Overview

The Instanssi Lights Control Protocol allows for the remote control of lights via UDP packets. This protocol is designed to be simple and easily implemented in various programming languages. The packet structure consists of a specification version, a nickname tag, and one or more effect commands.

## Packet Structure

A packet sent to the Instanssi Lights server follows this structure:

| Byte Position | Content                       | Description                                              |
|---------------|-------------------------------|----------------------------------------------------------|
| 0             | Specification Version         | The version of the protocol specification (always `1`).  |
| 1             | Nickname Start                | Indicates the start of the nickname (value `0`).         |
| 2 to N-1      | Nickname Characters           | ASCII values of the nickname characters, terminated by `0`. Maximum length including the termination is N. |
| N             | Nickname End                  | Indicates the end of the nickname (value `0`).           |
| N+1 to End    | Effect Commands               | One or more effect commands.                              |

### Effect Command Structure

Each effect command within a packet has the following structure:

| Byte Position | Content           | Description                                            |
|---------------|-------------------|--------------------------------------------------------|
| 0             | Effect Type       | The type of effect (e.g., `1` for light).              |
| 1             | Light Index       | The index of the light to control.                     |
| 2             | Extension Byte    | Currently unused, must be `0`.                         |
| 3             | Red Intensity     | The intensity of the red color component (0-255).      |
| 4             | Green Intensity   | The intensity of the green color component (0-255).    |
| 5             | Blue Intensity    | The intensity of the blue color component (0-255).     |

## Example

The following example demonstrates controlling the first light with maximum red intensity and no green or blue intensity:

```python
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packet = bytearray([
    1,    # Protocol version
    0,    # Nickname start
    101,  # 'e'
    112,  # 'p'
    101,  # 'e'
    108,  # 'l'
    105,  # 'i'
    0,    # Nickname end
    1,    # Effect type (light)
    0,    # Light index (first light)
    0,    # Extension byte
    255,  # Red intensity (max)
    0,    # Green intensity (none)
    0,    # Blue intensity (none)
])
udp_socket.sendto(packet, ('10.0.69.214', 9909))
```

## Notes

- The nickname is a unique identifier for the sender of the command.
- Multiple effect commands can be concatenated in a single packet to control multiple lights simultaneously.
- The protocol is designed for simplicity and ease of implementation across different programming languages.

## License

Original protocol description https://github.com/turol/valoserveri/blob/master/use_examples/over_udp.py

The MIT License (MIT)

Copyright (c) 2020 Instanssi.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
