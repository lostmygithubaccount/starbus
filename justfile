# list justfile recipes
default:
    just --list

preview:
    @quarto preview .

render:
    @quarto render .

upload:
    @az storage azcopy blob upload -c '$web' --account-name starbus -s "_book/*" --recursive
