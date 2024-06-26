"""Movimientos

Revision ID: 759e4e53f575
Revises: 
Create Date: 2024-06-08 20:21:26.722949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '759e4e53f575'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('detalles_movimiento')
    op.drop_table('venta')
    op.drop_table('movimiento')
    op.drop_table('tipo_movimiento')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipo_movimiento',
    sa.Column('id_tipo_movimiento', sa.INTEGER(), nullable=False),
    sa.Column('nombre', sa.VARCHAR(), nullable=False),
    sa.Column('descripcion', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id_tipo_movimiento')
    )
    op.create_table('movimiento',
    sa.Column('id_movimiento', sa.INTEGER(), nullable=False),
    sa.Column('id_tipo_movimiento', sa.INTEGER(), nullable=True),
    sa.Column('fecha_hora', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['id_tipo_movimiento'], ['tipo_movimiento.id_tipo_movimiento'], ),
    sa.PrimaryKeyConstraint('id_movimiento')
    )
    op.create_table('venta',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('id_libro', sa.INTEGER(), nullable=False),
    sa.Column('cantidad', sa.INTEGER(), nullable=False),
    sa.Column('precio', sa.FLOAT(), nullable=False),
    sa.Column('monto', sa.FLOAT(), nullable=False),
    sa.Column('fecha_venta', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['id_libro'], ['libro.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('detalles_movimiento',
    sa.Column('id_detalle_movimiento', sa.INTEGER(), nullable=False),
    sa.Column('id_movimiento', sa.INTEGER(), nullable=True),
    sa.Column('id_libro', sa.INTEGER(), nullable=True),
    sa.Column('cantidad', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['id_libro'], ['libro.id_libro'], ),
    sa.ForeignKeyConstraint(['id_movimiento'], ['movimiento.id_movimiento'], ),
    sa.PrimaryKeyConstraint('id_detalle_movimiento')
    )
    # ### end Alembic commands ###
