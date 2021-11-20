module.exports = {
  assetsDir: 'static',
  // publicPath: undefined,
  outputDir: 'templates',
  pages: {
    disciplina: {
      // entry for the page
      entry: 'src/views/disciplina/disciplina.js',
      // the source template
      template: 'public/disciplina.html',
      // output as dist/index.html
      filename: 'disciplina.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Disciplina Page'
    },
    home: {
      // entry for the page
      entry: 'src/views/home/home.js',
      // the source template
      template: 'public/home.html',
      // output as dist/index.html
      filename: 'home.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Home Page'
    },
    login: {
      // entry for the page
      entry: 'src/views/login/login.js',
      // the source template
      template: 'public/login.html',
      // output as dist/index.html
      filename: 'login.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Login Page'
    },
    profile: {
      // entry for the page
      entry: 'src/views/profile/profile.js',
      // the source template
      template: 'public/profile.html',
      // output as dist/index.html
      filename: 'profile.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Profile Page'
    },
    register: {
      // entry for the page
      entry: 'src/views/register/register.js',
      // the source template
      template: 'public/register.html',
      // output as dist/index.html
      filename: 'register.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Register Page'
    },
    adicionar_disciplina: {
      // entry for the page
      entry: 'src/views/adicionar_disciplina/adicionar_disciplina.js',
      // the source template
      template: 'public/adicionar_disciplina.html',
      // output as dist/index.html
      filename: 'adicionar_disciplina.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Adicionar Disciplina Page'
    }
  }
}
