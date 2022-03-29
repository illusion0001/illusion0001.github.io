current=`date '+%Y-%m-%d %H:%M:%S %A (%Z %z)'`
msg="Patches built on: \`$current\`"
patch_file="patch_built.md"
cp -r "_patch0" "patch0"
ls -R _patch0 > manifest_patch0.txt
find _patch0 -print > manifest_patch1.txt
echo $msg >> patch0/$patch_file
echo $msg >> _pages/$patch_file
cat patch0/$patch_file
cat _pages/$patch_file
zip -r _patch/patch.zip patch0
rm  -r "patch0"
