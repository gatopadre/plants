import { Injectable } from '@angular/core';
import { MongoClient } from 'mongodb';

@Injectable({
  providedIn: 'root'
})
export class MongoService {
  private client: MongoClient;
  private url: string = 'mongodb+srv://sebastianzunigasaavedra:<password>@plantapp.03vptpo.mongodb.net/?retryWrites=true&w=majority&appName=PlantAPP';

  constructor() {
    this.client = new MongoClient(this.url);
    this.connect();
  }

  async connect() {
    try {
      this.client = await MongoClient.connect(this.url);
      console.log('Conectado a MongoDB');
    } catch (error) {
      console.error('Error al conectar a MongoDB', error);
    }
  }

  async insertPlant(plantData: any) {
    const db = this.client.db('PlantApp');
    const collection = db.collection('Plants');
    await collection.insertOne(plantData);
    console.log('Planta insertada en MongoDB');
  }

  async disconnect() {
    if (this.client) {
      await this.client.close();
      console.log('Conexión cerrada');
    }
  }
}
