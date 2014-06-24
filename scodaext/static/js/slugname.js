
function slugify(s)
    {
        return s.toLowerCase().replace(/[^A-Za-z0-9-]/,"-")
        }

function slugifyName()
    {
        document.getElementsByName('slug')[0].value=slugify(this.value);
        }

document.getElementsByName('name')[0].onclick=slugifyName;