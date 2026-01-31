# How to Configure Grub2

Messing with your bootloader can be intimidating, but once you understand the pieces, it's quite straightforward.

## What is GRUB2?

GRUB stands for **GRand Unified Bootloader**. It's the first program that runs when you start your computer. Its main job is to load the Linux kernel into memory and then pass control over to it. GRUB2 is the current version.

## The Main Configuration File: `/etc/default/grub`

The primary file you'll edit to control GRUB's behavior is `/etc/default/grub`. This file contains key-value pairs that control the settings for your boot menu. After you change this file, you need to run a command to apply the changes.

Let's look at the most important parameters in this file.

### Main GRUB2 Parameters

*   `GRUB_DEFAULT`: This sets the default operating system or kernel to boot.
    *   `GRUB_DEFAULT=0`: Boots the first entry in the menu (numbering starts at 0).
    *   `GRUB_DEFAULT=saved`: Boots the entry that was last selected. This is useful if you frequently switch between OSes. You need to also set `GRUB_SAVEDEFAULT=true`.
    *   `GRUB_DEFAULT="Advanced options for Ubuntu>Ubuntu, with Linux 5.4.0-42-generic"`: You can also use the full menu entry title.

*   `GRUB_TIMEOUT`: The number of seconds the boot menu is displayed before automatically booting the default entry.
    *   `GRUB_TIMEOUT=5`: Waits for 5 seconds.
    *   `GRUB_TIMEOUT=-1`: Disables the timeout completely, waiting for you to make a choice.

*   `GRUB_TIMEOUT_STYLE`: Controls how the timeout is displayed.
    *   `menu`: The default, shows the full menu.
    *   `countdown`: Shows the menu with a visible countdown.
    *   `hidden`: Hides the menu during the timeout. You can press `ESC` to show it.

*   `GRUB_CMDLINE_LINUX`: Kernel parameters that are added to *all* Linux menu entries (including recovery modes).

*   `GRUB_CMDLINE_LINUX_DEFAULT`: Kernel parameters that are added *only* to the normal (non-recovery) Linux menu entries. This is where you often see parameters like `quiet` (to reduce boot messages) and `splash` (to show a splash screen).

*   `GRUB_DISABLE_OS_PROBER`: The `os-prober` script automatically detects other operating systems (like Windows) and adds them to the boot menu.
    *   `GRUB_DISABLE_OS_PROBER=false`: (Default) Allows `os-prober` to run.
    *   `GRUB_DISABLE_OS_PROBER=true`: Disables it. This is useful for faster boot times if you only have one OS, or for security reasons.

*   `GRUB_GFXMODE`: Sets the screen resolution for the GRUB menu itself. For example: `GRUB_GFXMODE=1920x1080`.

## Step-by-Step: How to Update Your GRUB2 Configuration

Let's put it all together.

### Step 1: Back Up Your Configuration

Before you start, it's always wise to back up the current configuration file.

```bash
sudo cp /etc/default/grub /etc/default/grub.bak
```

### Step 2: Edit the Configuration File

Open `/etc/default/grub` with your favorite text editor. You'll need `sudo` because this is a system file.

```bash
sudo nano /etc/default/grub
# Or if you prefer vim
# sudo vim /etc/default/grub
```

Now, make your desired changes. For example, let's say you want to change the timeout to 10 seconds. You would find the line `GRUB_TIMEOUT=5` and change it to `GRUB_TIMEOUT=10`.

### Step 3: Apply the Changes

This is the most crucial step. Editing `/etc/default/grub` does nothing on its own. You must run a command that takes your settings and uses them to generate the actual GRUB configuration file (`/boot/grub/grub.cfg`).

**Do not edit `/boot/grub/grub.cfg` directly!** It is automatically generated and your changes will be overwritten.

The command you need to run depends on your Linux distribution:

*   **For Debian, Ubuntu, and their derivatives:**
    A handy wrapper script is provided.

    ```bash
    sudo update-grub
    ```

*   **For Arch Linux, Fedora, RHEL, CentOS, and others:**
    You need to call the `grub-mkconfig` command directly and specify the output file.

    ```bash
    sudo grub-mkconfig -o /boot/grub/grub.cfg
    ```

After the command finishes, your new configuration is live.

### Step 4: Reboot and Verify

Reboot your system to see your changes in action.

```bash
reboot
```

You should now see the GRUB menu reflect the new settings you've applied.

---

And that's it! You now know how to safely edit your GRUB2 configuration. Remember the golden rule: edit `/etc/default/grub`, then run the update command. Happy booting!
