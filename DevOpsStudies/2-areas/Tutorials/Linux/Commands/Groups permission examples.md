## Checking our groups

Let’s see our groups

![[linux_create_group_example.png]]

We have 3 groups: jvictor, wheel and docker

## Working with Groups

- New files belong to your primary group
- The `chgrp` command changes the group

List all groups on the system

```bash
groups
```

Create a new group

```bash
groupadd <group_name>
```

Change a file or directory to another group

```bash
chgrp <groupname> <filename>
```

Use case:

- Group: admin
- Filename: file.txt, new.txt, old.txt

```bash
chgrp admin *.txt
```

---

### Modifying and Deleting Groups

**Rename a group:**

You can rename a group using the `groupmod` command with the `-n` flag. Let's rename `oldgroup` to `newgroup`.

```bash
sudo groupmod -n newgroup oldgroup
```
*Note: This does not automatically update the group for files created with the old group name. You would need to change those manually with `chgrp`.*

**Add a user to a group:**

To add an existing user to a group, use the `usermod` command. This is useful for granting permissions (e.g., adding a user to the `docker` or `sudo` group).

```bash
# -aG means "append" to "secondary groups"
sudo usermod -aG <group_name> <user_name>
```
The user will need to log out and log back in for the change to take effect.

**Remove a user from a group:**

You can use the `gpasswd` command with the `-d` flag to remove a user from a group.

```bash
sudo gpasswd -d <user_name> <group_name>
```

**Delete a group:**

To delete a group, use the `groupdel` command.

```bash
sudo groupdel <group_name>
```
*Note: You cannot delete the primary group of an existing user. You must change the user's primary group first.*