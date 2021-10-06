
function getArea(length, width) {
    const area = length*width;
    
    
    return area;
}

function getPerimeter(length, width) {
    const perimeter = (2*length) + (2*width);
    
    
    return perimeter;
}

function main() {
    const length = +'20';
    const width = +'10';
    
    console.log(getArea(length, width));
    console.log(getPerimeter(length, width));
}


main();
