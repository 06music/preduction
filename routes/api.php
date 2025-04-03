<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ForebetController;

Route::get('/forebet', [ForebetController::class, 'index']);
