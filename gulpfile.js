var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var gzip = require('gulp-gzip');
var gutil = require('gulp-util');

var dirs = {
  src: {
    style: 'hourglass_site/static_source/style/',
  },
  dest: {
    style: 'hourglass_site/static/hourglass_site/style/',
  }
};

var paths = {
  sass: '**/*.scss',
};

// run in production mode with the `--production` flag
// ex: `npm run gulp -- build --production`
var isProd = !!gutil.env.production;
gutil.log('Running in',
  gutil.colors.cyan(isProd ? 'PRODUCTION' : 'DEVELOPMENT'),
  'mode'
);

var gzip_options = {
    threshold: '1kb',
    gzipOptions: {
        level: 9
    }
};

// running `gulp` will default to watching and dist'ing files
gulp.task('default', ['watch']);

// TODO: production build
// Will need to run before collectstatic
gulp.task('build', ['sass']);


/* Compile Our Sass */
gulp.task('sass', function () {
    return gulp.src(dirs.src.style + paths.sass)
        .pipe(sass())
        .pipe(gulp.dest(dirs.dest.style))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest(dirs.dest.style))
        .pipe(gzip(gzip_options))
        .pipe(gulp.dest(dirs.dest.style));
});

/* Watch Files For Changes */
gulp.task('watch', ['sass'], function () {
    gulp.watch(dirs.src.style + paths.sass, ['sass']);
});
