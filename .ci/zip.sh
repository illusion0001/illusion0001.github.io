patch_file=patch_built.md
cp -r _patch0 patch0
ls -R _patch0 > manifest_patch0.txt
find _patch0 -print > manifest_patch1.txt
curl https://raw.githubusercontent.com/illusion0001/console-game-patches/gh-pages/$patch_file
cat $patch_file > patch0/$patch_file
cat $patch_file > _pages/$patch_file
cat patch0/$patch_file
zip -r _patch/patch.zip patch0
rm  -r patch0
