<?php

use Illuminate\Support\Facades\Route;
use Inertia\Inertia;
use App\Http\Controllers\ForebetController; // ✅ Add this line
use App\Http\Controllers\ForebetScraperController; // ✅ Add this line


Route::get('/', function () {
    return Inertia::render('Home');
});

Route::get('/forebet-data', [ForebetController::class, 'getMatches']);

Route::get('/run-scraper', [ForebetScraperController::class, 'run']);

Route::get('dashboard', function () {
    return Inertia::render('Dashboard');
})->middleware(['auth', 'verified'])->name('dashboard');

require __DIR__.'/settings.php';
require __DIR__.'/auth.php';
