import { Component, OnInit } from '@angular/core';
import { UsuarioService } from 'src/app/services/usuario.service';
import { TarefaService } from 'src/app/services/tarefa.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Usuario } from 'src/app/models/usuario.model';
import { Tarefa } from 'src/app/models/tarefa.model';

@Component({
  selector: 'app-usuario-details',
  templateUrl: './usuario-details.component.html',
  styleUrls: ['./usuario-details.component.css']
})
export class UsuarioDetailsComponent implements OnInit {
  currentUsuario: Usuario = {
    nome: ''
  };

  currentTarefa: Tarefa = {
    descricao: '',
    estadoTarefa: '',
  };

  tarefa: Tarefa = {
    descricao: '',
    estadoTarefa: 'Pendente'
  };

  message = '';

  tarefas?: Tarefa[];
  currentIndex = -1;

  constructor(
    private usuarioService: UsuarioService,
    private tarefaService: TarefaService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.message = '';
    this.getUsuario(this.route.snapshot.params.id);
  }

  getUsuario(id: string): void {
    this.usuarioService.get(id)
      .subscribe(
        data => {
          this.currentUsuario = data;
          this.findTarefaByUsuario();
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  updateUsuario(): void {
    this.usuarioService.update(this.currentUsuario.id, this.currentUsuario)
      .subscribe(
        response => {
          console.log(response);
          this.message = response.message;
        },
        error => {
          console.log(error);
        });
  }

  findTarefaByUsuario(): void {
    this.tarefaService.findTarefaByUsuario(this.currentUsuario.id)
      .subscribe(
        data => {
          this.tarefas = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  deleteUsuario(): void {
    this.usuarioService.delete(this.currentUsuario.id)
      .subscribe(
        response => {
          console.log(response);
          this.router.navigate(['/usuarios']);
        },
        error => {
          console.log(error);
        });
  }

  saveTarefa(): void {
    const data = {
      descricao: this.tarefa.descricao,
      usuario: this.currentUsuario.id,
      estadoTarefa: 'Pendente'
    };

    this.tarefaService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.refreshList();
        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.findTarefaByUsuario();
    this.currentTarefa = undefined;
    this.currentIndex = -1;
  }

  setActiveTarefa(tarefa: Tarefa, index: number): void {
    this.currentTarefa = tarefa;
    this.currentIndex = index;
  }

  updateEstadoTarefa(): void {
    console.log(this.currentTarefa.estadoTarefa);
    this.currentTarefa.estadoTarefa == 'Pendente' ? this.currentTarefa.estadoTarefa = 'Feito' : this.currentTarefa.estadoTarefa = 'Pendente';
    this.tarefaService.update(this.currentTarefa.id, this.currentTarefa)
      .subscribe(
        response => {
          console.log(response);
          this.message = response.message;
        },
        error => {
          console.log(error);
        });
  }
}
