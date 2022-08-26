export class Node {
    constructor(data){
        this.data = data;
        this.next = null;
        // Copy List w/ Random Pointer Problem
        this.random = null;
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

