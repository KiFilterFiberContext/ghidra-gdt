# GDT Exporter for Ghidra
Ghidra script for generating Ghidra Data Type (GDT) archives containing type and symbol information

Inspired by [this post](https://posts.specterops.io/methodology-for-static-reverse-engineering-of-windows-kernel-drivers-3115b2efed83), I decided to make an alternative method of generating GDT archives to aid my windows kernel driver reverse engineering process.  Ghidra Data Type (GDT) archives are used for storing function data type and symbol information and can be imported in different Ghidra projects through the Data Type Manager.

There wasn't much documentation about it but I found one article about the topic from [Stack Overflow](https://reverseengineering.stackexchange.com/questions/27019/ghidra-add-data-types-from-open-source-project/27024) and decided to port the script over to python with a few minor adjustments.  Ghidra also supports transferring data types through `Capture Function Data Types` but I preferred using this method.

Included in the repository are pregenerated GDT archives for various system images from Windows 11 Insider Dev Build 22504 including `kernelbase`, `ntoskrnl` and `ntdll`.

## Installation
- Copy `ExportGDT.py` into `$GHIDRA_ROOT\Ghidra\Features\FunctionID\ghidra_scripts`

## Usage
- Open the desired file in Ghidra containing PDB/DWARF debug info
- Run this script and select the `.gdt` output file
- Open the other program and open the `Data Type Manager`
- Click on the dropdown and select `Open File Archive...`
- Select the `.gdt` archive then right click and select `Apply Function Data Types`

## Credits
- [ghidra-data](https://github.com/0x6d696368/ghidra-data) by 0x6d696368
- [Easily getting type information of a common ELF library into Ghidra](https://reversing.technology/2021/06/16/ghidra_DWARF_gdt.html) 
