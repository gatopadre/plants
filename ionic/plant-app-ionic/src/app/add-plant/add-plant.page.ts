import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-add-plant',
  templateUrl: './add-plant.page.html',
  styleUrls: ['./add-plant.page.scss'],
})
export class AddPlantPage implements OnInit {

  plantName: string = '';

  constructor(private router: Router, private http: HttpClient) { }

  ngOnInit() {
  }

  async guardarPlanta(form: NgForm) {
    if (form.invalid) {
      // Si el formulario es inválido, no hacemos nada
      return;
    }

    const plantData = {
      name: this.plantName,
      // Agrega más datos de la planta según sea necesario
    };
    // Hacer la solicitud POST al endpoint de FastAPI
    this.http.post('http://localhost:8000/plant', plantData).subscribe({
      next: () => {
        console.log('Planta guardada:', this.plantName);
        // Después de guardar la planta, puedes navegar de regreso a la pantalla principal
        this.router.navigate(['/home']);
      },
      error: (error) => {
        console.error('Error al guardar la planta:', error);
        // Manejar el error según sea necesario
      }
    });
  }

  volverHome() {
    console.log('Volviendo al home:', this.plantName);
    this.router.navigate(['/home']);
  }

}
