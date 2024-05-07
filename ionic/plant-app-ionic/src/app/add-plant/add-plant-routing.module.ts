import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AddPlantPage } from './add-plant.page';

const routes: Routes = [
  {
    path: '',
    component: AddPlantPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AddPlantPageRoutingModule {}
