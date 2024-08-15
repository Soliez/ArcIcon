# Arc Browser Icon Changer

![arc icons](https://i.imgur.com/u93MRIy.png)

A python script for manually changing the Arc Browser icon on macOS.


## Installation

### Step 1: Clone this repository

```bash
git clone https://github.com/Soliez/ArcIcon.git
```

### Step 2: Add the following line to your shell profile (Optional but recommended)

```bash
alias arcicon="/usr/bin/python3 <script-path>"
```
Replace `<script-path>` with the full path to the `arcicon.py` on your computer.

This step is optional but it allows you execute `arcicon` from any location without having to specify the python interpreter and path to the script each time you run it.

## Usage

```bash
arcicon set <icon-name>
```
Replace `<icon-name>` with any of the following options:
- `original`
- `candy`
- `hologram`
- `neon`
- `flutedGlass`
- `schoolbook`
- `colorful`

<br>

After running `arcicon`, restart Arc to see the applied change.

## Demonstration
![demo gif](media/arcicon-demo.gif)