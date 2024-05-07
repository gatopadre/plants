import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AddPlantPageRoutingModule } from './add-plant-routing.module';

import { AddPlantPage } from './add-plant.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    AddPlantPageRoutingModule
  ],
  declarations: [AddPlantPage]
})
export class AddPlantPageModule {}
