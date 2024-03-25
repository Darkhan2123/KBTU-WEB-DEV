import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Product, products } from '../products';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {
  @Input() item!: Product;
  @Output() remove = new EventEmitter();
  like: number = 0;
  isLiked: boolean = false; // Track whether the item is liked or not

  share(url : string) {
    var otvet = window.prompt()
    var link = "https://t.me/share/url?url="+url+"&text=" + otvet;
    window.open(link);
  }

  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }

  deleteItem(){
    this.remove.emit(this.item.id);
  }
  
  likeUp(id: number){
    if (!this.isLiked) {
      this.like++;
    } else {
      this.like--;
    }
    this.isLiked = !this.isLiked;
  }
}
