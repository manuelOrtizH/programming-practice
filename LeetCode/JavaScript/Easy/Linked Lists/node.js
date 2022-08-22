export class Node {
    constructor(data){
        this.data = data;
        this.next = null;
    }

    display(){
        let actual = this;
        const dataList = [];
        while (actual != null){
            dataList.push(actual.data);
            actual = actual.next;
        }

        console.log(dataList);
    }

    append(...args){
        
        let actual = this;
        args.map(el => {
            while (actual.next != null){
                actual = actual.next;
            }
            actual.next = new Node(el);
        });
    }
}


const head = new Node(1)
head.append(1,2,3)
head.display()